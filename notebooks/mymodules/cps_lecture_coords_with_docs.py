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

# %%
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

# %%
di = DrawInterface()

# %%
vis_cds = mkshapes.makeCoords(length=0.35, lineWidth=6)
cds = coordinates()

# %%
di.addObject(vis_cds)
di.addObject(mkshapes.makeCoords(length=3.0, lineWidth=2))

# %%
# %display

# %% [markdown]
# ## プロパティ
# https://irsl-tut.github.io/irsl_documents/ja/coordinates.html#properties

# %% [markdown]
# #### pos

# %%
cds.pos

# %%
cds.pos = fv(0.5, -0.5, 1.0)

# %%
cds

# %%
vis_cds.newcoords(cds)

# %% [markdown]
# #### rot

# %%
cds.rot

# %%
cds.rot = fv([0, 1, 0],[1, 0, 0],[0, 0, -1])

# %%
vis_cds.newcoords(cds)

# %% [markdown]
# #### x_axis

# %%
cds.x_axis

# %% [markdown]
# #### y_axis

# %%
cds.y_axis

# %% [markdown]
# #### z_axis

# %%
cds.z_axis

# %% [markdown]
# #### quaternion

# %%
cds.quaternion

# %%
cds.quaternion = fv(0, 0, 0, 1.0)

# %%
vis_cds.newcoords(cds)

# %% [markdown]
# #### RPY

# %%
cds.RPY

# %%
cds.RPY = fv(0, 0, -0.8)

# %%
vis_cds.newcoords(cds)

# %% [markdown]
# #### angleAxis

# %%
cds.angleAxis

# %%
cds.angleAxis = fv(1, 0, 0, 1.2)

# %%
cds

# %%
vis_cds.newcoords(cds)

# %% [markdown]
# #### homogeneousTransformation
#
#

# %%
cds.cnoidPosition

# %%
cds.cnoidPosition = fv([0, 1, 0, -0.5],[1, 0, 0, -0.5],[0, 0, -1, 0], [0, 0, 0, 1])

# %%
cds

# %%
vis_cds.newcoords(cds)

# %% [markdown]
# ## 変換したベクトルを返すメソッド(元のベクトルを変更しない)
# https://irsl-tut.github.io/irsl_documents/ja/coordinates.html#methods-to-convert-a-vector

# %%
cds.RPY = fv(0.5, -0.5, 1)
cds.pos = fv(0.4, -0.3, 0.8)
cds

# %% [markdown]
# #### rotate_vector

# %%
v = fv(1., 1., 1.)
res0 = cds.rotate_vector(v)
v

# %%
res0

# %% [markdown]
# #### invese_rotate_vector

# %%
v = fv(1., 1., 1.)
res1 = cds.inverse_rotate_vector(v)
v

# %%
res1

# %%
cds.inverse_rotate_vector(res0)

# %% [markdown]
# #### transform_vector

# %%
v = fv(0.1, 0.2, 0.3)
res0 = cds.transform_vector(v)
v

# %%
res0

# %% [markdown]
# #### inverse_transform_vector
#
#

# %%
v = fv(0.1, 0.2, 0.3)
res1 = cds.inverse_transform_vector(v)
v

# %%
res1

# %%
cds.inverse_transform_vector(res0)

# %% [markdown]
# ## ベクトルを座標系を使って変換するメソッド（元のベクトルを変更する）
# https://irsl-tut.github.io/irsl_documents/ja/coordinates.html#methods-to-convert-a-vector-change-input-value

# %% [markdown]
# #### rotateVector

# %%
v = fv(1., 1., 1.)
res0 = cds.rotateVector(v)
v

# %% [markdown]
# #### inverseRotateVector

# %%
v = fv(1., 1., 1.)
res1 = cds.inverseRotateVector(v)
v

# %%
cds.inverseRotateVector(res0)

# %%
res0

# %% [markdown]
# #### transformVector

# %%
v = fv(1., 1., 1.)
res0 = cds.transformVector(v)
v

# %% [markdown]
# #### inverseTransformVector
#
#

# %%
v = fv(1., 1., 1.)
res1 = cds.inverseTransformVector(v)
v

# %%
cds.inverseTransformVector(res0)

# %%
res0

# %% [markdown]
# ## 座標系を返すメソッド(自身のインスタンスの値を変更しない)
# https://irsl-tut.github.io/irsl_documents/ja/coordinates.html#methods-to-return-a-coordinate-without-modifying-itself

# %% [markdown]
# #### inverse_transformation

# %%
cds.inverse_transformation()

# %%
cds.inverse_transformation().transform(cds)

# %% [markdown]
# #### transformation

# %%
cds2 = coordinates(fv(0.5, 0.5, 0.5), fv(0, math.sqrt(0.5), math.sqrt(0.5), 0))

# %%
cds.transformation(cds2)

# %%
cds.get_transformed(cds.transformation(cds2))

# %% [markdown]
# #### mid_coords

# %%
cds.mid_coords(0.5, cds2)

# %% [markdown]
# #### get_transformed
#
#

# %%
cds.get_transformed(cds2)

# %%
cds.get_transformed(cds2).transform(cds2.inverse_transformation()).equal(cds)

# %% [markdown]
# ## 自身のインスタンスの値を変更するメソッド
# https://irsl-tut.github.io/irsl_documents/ja/coordinates.html#methods-to-modify-itself

# %% [markdown]
# #### newcoords

# %%
cds2.newcoords(cds)

# %%
cds2.equal(cds)

# %% [markdown]
# #### move_to
# under construction

# %% [markdown]
# #### translate

# %%
vis_cds.newcoords(cds2)

# %%
cds2.translate(fv(0, 0, 0.5))

# %%
vis_cds.newcoords(cds2)

# %%
cds2.newcoords(cds)
vis_cds.newcoords(cds2)

# %%
cds2.translate(fv(0, 0, 0.5), wrt=coordinates.wrt.world)

# %%
vis_cds.newcoords(cds2)

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# #### locate
# under construction

# %% [markdown]
# #### rotate

# %%
cds2.rotate(1.0, coordinates.Z)

# %%
vis_cds.newcoords(cds2)

# %%
cds2.rotate(0.5, coordinates.X, wrt = coordinates.wrt.world)

# %%
vis_cds.newcoords(cds2)

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# #### rotate_with_matrix
# rotate self coordinates by rotation matrix

# %% [markdown]
# #### orient
# translate <-> locate
#
# rotate <-> orient
#
# (relative <-> absolute)

# %% [markdown]
# #### orient_with_matrix
# orient self coordinates by rotation matrix

# %% [markdown]
# #### inverse

# %%
cpy_cds = cds.copy()

# %%
cds.inverse()

# %%
cpy_cds.transform(cds)

# %% [markdown]
# #### transform

# %%
cds1 = coordinates(fv(0.5, 0.5, 0.3))
cds1.rotate(PI/2, coordinates.X)

# %%
cds2 = coordinates(fv(0.1, 0.5, 0))
cds2.rotate(PI/4, coordinates.Z)

# %%
di.clear()
di.addObject(mkshapes.makeCoords(length=3.0, lineWidth=2))

# %%
aa = mkshapes.makeCoords(coords=cds1,  length=0.3, lineWidth=4)
bb = mkshapes.makeCoords(coords=cds2, length=0.3, lineWidth=8)
di.addObjects((aa, bb))

# %%
res = cds1.copy()
res.transform(cds2)

# %%
di.addObject(mkshapes.makeCoords(coords=res, length=0.3, lineWidth=4))

# %%
cds1.transformation(res)

# %% [markdown]
# $cds1 \rightarrow A$
#
# $cds2 \rightarrow B$
#
# 定義より
#
# $ A.trasnsform(B) \rightarrow AB $
#
# 確認式
#
# $ A.transformation(AB) \rightarrow A^{-1} AB = B $

# %%
ln1 = mkshapes.makeLineAxis(fv(0.,0,0), cds2.pos, axis_length=0.08, lineWidth=2)

# %%
ln2 = mkshapes.makeLineAxis(cds1.pos, res.pos, axis_length=0.08, lineWidth=2)

# %%
di.addObjects((ln1, ln2))

# %%
res = cds1.copy()
res.transform(cds2, wrt = coordinates.wrt.world)

# %%
# %display

# %%
di.clear()
di.addObject(mkshapes.makeCoords(length=3.0, lineWidth=2))
di.addObjects((aa, bb))

# %%
res = cds1.copy()
res.transform(cds2, wrt = coordinates.wrt.world)

# %%
di.addObject(mkshapes.makeCoords(coords=res, length=0.3, lineWidth=4))

# %%
cds2.transformation(res)

# %% [markdown]
# 定義より
#
# $ A.trasnsform(B, wrt=world) \rightarrow BA $
#
# 確認式
#
# $ B.transformation(BA) \rightarrow B^{-1} BA = A $
#

# %%
di.addObject(mkshapes.makeCoords(coords=res, length=0.3, lineWidth=4))

# %%
ln1 = mkshapes.makeLineAxis(fv(0.,0,0), cds1.pos, axis_length=0.08, lineWidth=2)
ln2 = mkshapes.makeLineAxis(cds2.pos, res.pos, axis_length=0.08, lineWidth=2)
di.addObjects((ln1, ln2))

# %%
# %display
