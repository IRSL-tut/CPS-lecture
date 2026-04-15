# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Robot Programming
#     language: python
#     name: roboprog
# ---

# %% [markdown]
# # リンク座標系

# %%
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

# %% [markdown]
# ## 座標系の準備
#
# - 原点: org
# - 座標系1 : sigma1
# - 座標系2 : sigma2
# - 原点から座標系1への変換: T0_1 (原点座標系で表される)
# - 座標系1から座標系2への変換: T1_2 (1座標系で表される)
# - 座標系2からエンドエフェクタへの変換: T2_ee (2座標系で表される)

# %%
org=coordinates()
T0_1=coordinates(fv(0, 0.5, 0.5))
T1_2=coordinates(fv(0, 0.5, 0))
T1_2.rotate(PI/4, coordinates.X)
T2_ee=coordinates(fv(0, 0.2, 0.2))

# %% [markdown]
# #### transformの小話
# transformメソッドはオブジェクトを変更してしまうので、copy()メソッドを使って元の値のコピーを変更する

# %%
old_cds = org.copy()
trs = T0_1.copy()

# %%
new_cds1 = old_cds.copy().transform(trs)
new_cds2 = old_cds.get_transformed(trs)

# %%
new_cds1

# %%
new_cds1.equal(new_cds2)

# %%
old_cds

# %%
old_cds.transform(trs)

# %%
old_cds

# %%
new_cds1.equal(old_cds)

# %% [markdown]
# ### 座標系1

# %%
sigma1=org.get_transformed(T0_1)

# %%
sigma1

# %% [markdown]
# ### 座標系2

# %%
sigma2=sigma1.get_transformed(T1_2)

# %%
sigma2

# %% [markdown]
# ### エンドエフェクタ

# %%
sigmaEE=sigma2.get_transformed(T2_ee)

# %%
sigmaEE

# %% [markdown]
# ## 座標系の表示

# %%
di = DrawInterface()

# %%
di.addObjects(mkshapes.makeCoords(coords=coordinates(), length=0.5, lineWidth=5))

# %%
di.addObjects(mkshapes.makeCoords(coords=sigma1, length=0.5, lineWidth=5))

# %%
di.addObjects(mkshapes.makeCoords(coords=sigma2, length=0.5, lineWidth=5))

# %%
di.addObjects(mkshapes.makeCoords(coords=sigmaEE, length=0.5, lineWidth=5))

# %%
# %display

# %% [markdown]
# ## 練習問題
# sigma1を動かして、sigmaEEがorgと一致するようにしてみよう
#
# (ここでは、原点からの座標系1の変換 T0_1 のみを変更する)

# %%
T1_ee=sigma1.transformation(sigmaEE)

# %%
T1_ee

# %% [markdown]
# 解答の計算

# %%
T0_1=T1_ee.inverse_transformation()

# %% [markdown]
# 解答を使った座標系の計算

# %%
sigma1=org.get_transformed(T0_1)

# %%
sigma2=sigma1.get_transformed(T1_2)

# %%
sigmaEE=sigma2.get_transformed(T2_ee)

# %% [markdown]
# エンドエフェクタ位置の確認

# %%
sigmaEE

# %% [markdown]
# 解答の表示

# %%
di.clear()

# %%
di.addObjects(mkshapes.makeCoords(coords=sigmaEE, length=0.5, lineWidth=5))

# %%
di.addObjects(mkshapes.makeCoords(coords=sigma2, length=0.5, lineWidth=5))

# %%
di.addObjects(mkshapes.makeCoords(coords=sigma1, length=0.5, lineWidth=5))

# %%
# %display

# %% [markdown]
# ### 練習問題の別解
#
# DrawInterfaceの原点を移動させて同様な表示となるか確認する。

# %%
di1 = DrawInterface()

# %%
sigma1=coordinates()
di1.addObjects(mkshapes.makeCoords(coords=sigma1, length=0.5, lineWidth=5))

# %%
sigma2=sigma1.get_transformed(T1_2)
di1.addObjects(mkshapes.makeCoords(coords=sigma2, length=0.5, lineWidth=5))

# %%
sigmaEE=sigma2.get_transformed(T2_ee)
di1.addObjects(mkshapes.makeCoords(coords=sigmaEE, length=0.5, lineWidth=5))

# %%
# %display

# %% [markdown]
# 座標系を動かしてみる

# %%
di1.translate(fv(0,0,0.5))

# %%
di1.rotate(-PI/6, coordinates.X)

# %% [markdown]
# この時のエンドエフェクタの位置

# %%
di1.get_transformed(T1_ee)

# %% [markdown]
# 解答の確認

# %%
di1.newcoords(T0_1)

# %% [markdown]
# エンドエフェクタ位置の確認

# %%
di1.get_transformed(T1_ee)

# %%
# %display
