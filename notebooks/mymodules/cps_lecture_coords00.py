# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Choreonoid
#     language: python
#     name: choreonoid
# ---

# %% [markdown]
# # 3次元座標系

# %%
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

# %% [markdown]
# ## 3次元位置
# `numpy.array([x,y,z])` として3次元のベクトルを作ります。
#
# `from numpy import array as npa` となっているので `npa` と書けます。
#
# または、`fv(x, y, z)` が `numpy.array([x, y, z])` となります。

# %%
pos = fv(1, 2, 3)

# %%
pos

# %%
v0 = fv(1, 1, 0)
v1 = fv(2, 2, -2)

# %% [markdown]
# ### ベクトルの足し算

# %%
v0 + v1

# %% [markdown]
# ### スカラー積

# %%
3 * v0

# %% [markdown]
# ## 3次元の回転
# 3次元の回転は3x3行列で表されます。
#
# 3要素のリスト３つのリストとして 3x3行列を作ります。

# %%
rot = fv([1,0,0],[0,1,0],[0,0,1])

# %%
rot

# %% [markdown]
# ### クオータニオン
# (x, y, z, w) で表記

# %%
q = IC.rotationToQuaternion(rot)

# %%
q

# %% [markdown]
# ### AngleAxis
# 軸周りの回転
#
# coordinatex.X, coordinatex.Y, coordinatex.Z はそれぞれ、x軸,y軸,z軸を表す3次元ベクトルです。
# [1, 0, 0]軸 (x軸) の周りに pi/3 [radian] 回転させる

# %%
arot = IC.angleAxisNormalized(PI/3, coordinates.X)

# %%
PI

# %%
arot

# %% [markdown]
# ### ベクトルの回転
#
# Matrix(3x3) x vector(1x3)
#
# Matrix.dot(vector)

# %%
arot.dot(v1)

# %% [markdown]
# ## 3次元の座標系
# 以下の資料を参照してください。
#
# [3次元座標系の説明](https://irsl-tut.github.io/irsl_documents/ja/coordinates.html)
#
# [pythonでのcoordinatesの使い方](https://irsl-tut.github.io/irsl_documents/ja/module_cnoid_irslcoords.html#class-cnoid-irslcoords-coordinates)

# %% [markdown]
# ### 座標系の生成

# %%
cds = coordinates(pos, rot)

# %%
cds

# %% [markdown]
# #### 等価性の評価(同じもの)

# %%
c0=cds
c0 is cds

# %%
c0

# %%
cds

# %%
c1 = coordinates(pos, rot)

# %%
c1

# %% [markdown]
# #### 等価性の評価(値が同じ)

# %%
c0.equal(c1, 1e-20)

# %%
c0 is c1

# %% [markdown]
# coordinatesの表示は <coordinates[address] x y z / qx qy qz qw> となっています。
#
# x, y, zは3次元の位置、qx, qy, qz, qw は回転を表すクオータニオンです。

# %%
cds.rot = arot

# %%
cds

# %% [markdown]
# ### 座標系のデータアクセス

# %%
cds.pos

# %%
cds.rot

# %% [markdown]
# #### ロールピッチヨー角

# %%
cds.getRPY()

# %% [markdown]
# #### クオータニオン

# %%
cds.quaternion

# %% [markdown]
# #### AngleAxis

# %%
cds.getRotationAngle()

# %% [markdown]
# ### 座標系の移動

# %%
cds2 = coordinates()

# %%
cds2.translate(fv(0, 1, 0))

# %% [markdown]
# ### 座標系の回転

# %%
cds2.rotate(PI/3, coordinates.X)

# %% [markdown]
# ### 同次変換行列(Homogeneous transformation matrix)
# ```
# T = | Rot p |
#     | 0   1 |
# ```

# %%
cds2.cnoidPosition

# %% [markdown]
# ### 同次変換行列の計算
# T1, T2は以下のようになります。
# ```
# T1 = | R1 p1 |
#      | 0   1 |
# ```
#
# ```
# T2 = | R2 p2 |
#      | 0   1 |
# ```
#
# T1とT2の掛け算は以下のようになります。
# ```
# T1 * T2  = | R1R2  R1p2 + p1 |
#            |    0      1     |
# ```
#

# %%
Rot1 = IC.angleAxisNormalized( PI/3, coordinates.X)
Rot2 = IC.angleAxisNormalized(-PI/4, coordinates.Y)
pos1 = fv( 1,  2,  3)
pos2 = fv(-3, -1, -2)
cds1 = coordinates(pos1, Rot1)
cds2 = coordinates(pos2, Rot2)

# %%
cds1.cnoidPosition

# %%
cds2.cnoidPosition

# %%
cds1.cnoidPosition.dot(cds2.cnoidPosition)

# %%
Rot1.dot(Rot2)

# %%
Rot1.dot(pos2) + pos1

# %%
cds_a = coordinates(Rot1.dot(pos2) + pos1, Rot1.dot(Rot2))

# %%
cds_b = cds1.get_transformed(cds2)

# %%
cds_a

# %%
cds_b

# %%
cds_a.equal(cds_b)

# %%
cds_a.cnoidPosition

# %% [markdown]
# ## 座標系の表示

# %% [markdown]
# ### 表示用のオブジェクト
# DrawInterfaceを使う。
#
# `from irsl_choreonoid.draw_coords import GeneralDrawInterfaceWrapped as DrawInterface` とインポートされている。
#
# mkshapes.makeCoords(coords, length, lineWidth) で表示用のオブジェクトを作成。
#
# lengthは矢印の長さ[m], lineWidthは矢印の太さ[pixel] となっています。

# %%
di = DrawInterface()

# %% [markdown]
# ### addCoords 表示座標の追加

# %%
c_org = mkshapes.makeCoords(length = 0.5, lineWidth=5)

# %%
c_cds2 = mkshapes.makeCoords(coords=cds2, length = 0.5, lineWidth=5)

# %%
di.addObjects((c_org, c_cds2))

# %% [markdown]
# ### 画面のファイル化
# `%display` とすると、表示画面がnotebookにダウンロードできます。
#
# これはpythonのコマンドではありません。
#
# 本講義のchoreonoidを使ったjupyterのみで使えるコマンドです。

# %%
# %display

# %% [markdown]
# ### 座標系の表示を消す

# %%
di.clear()

# %%
# %display

# %% [markdown]
# ### 座標系の表示の移動
# di を、translate, rotate, transform, newcoords のメソッドで位置を変更すると、表示座標系の基準を移動させることができる。

# %%
di.addObjects((c_org, c_cds2))

# %%
cds2.translate(fv(0, 0.5, 0.5))

# %%
c_cds2.newcoords(cds2)

# %%
# %display

# %% [markdown]
# 原点を移動させます

# %%
di.translate(fv(0, 0, 0.6))

# %%
# %display

# %% [markdown]
# 原点を回転させます。
#
# y軸周りにPI/4の回転

# %%
di.rotate(PI/8, coordinates.Y)

# %%
# %display

# %% [markdown]
# # (以下古いので注意) 表示用のオブジェクト
#
# `from irsl_choreonoid.draw_coords import DrawCoordsListWrapped as DrawCoords` となっている。
#
# DrawCoords(length, width) で表示用のオブジェクトを作成。
#
# lengthは矢印の長さ[m], widthは矢印の太さ[pixel] となっています。

# %%
dc = DrawCoords(length=0.5, width=5)

# %%
org = coordinates()

# %% [markdown]
# ### addCoords 表示座標の追加

# %%
dc.addCoords(org)

# %%
dc.addCoords(cds2)

# %% [markdown]
# ### 画面のファイル化
# `%display` とすると、表示画面がnotebookにダウンロードできます。
#
# これはpythonのコマンドではありません。
#
# 本講義のchoreonoidを使ったjupyterのみで使えるコマンドです。

# %%
# %display

# %% [markdown]
# ### 座標系の表示を消す

# %%
dc.clear()

# %%
# %display

# %% [markdown]
# ### 座標系の表示の移動
# dc を、translate, rotate, transform, newcoords のメソッドで位置を変更すると、表示座標系の基準を移動させることができる。

# %%
cds2.translate(fv(0, 0.5, 0.5))

# %%
dc.addCoords(coordinates())

# %%
dc.addCoords(cds2)

# %%
# %display

# %% [markdown]
# 原点を移動させます

# %%
dc.translate(fv(0, 0, 0.6))

# %%
# %display

# %% [markdown]
# 原点を回転させます。
#
# y軸周りにPI/4の回転

# %%
dc.rotate(PI/8, coordinates.Y)

# %%
# %display
