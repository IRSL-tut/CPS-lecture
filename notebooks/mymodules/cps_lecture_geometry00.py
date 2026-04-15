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
# # 幾何構造を作る

# %%
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

# %% [markdown]
# ## 表示用のオブジェクト
# DrawInterface を作る。 DrawCoordsと同じような働きをする。

# %%
di = DrawInterface()

# %% [markdown]
# ### BOXを作る
# 最初の3つのパラメータは、x,y,z軸方向の辺の長さ。colorはRed, Blue, Greenを表すリストで、それぞれの数字は0から1数字。
#
# ```mkshapes.makeBox(0.5, 0.5, 0.5, color = [0, 1, 0])```

# %%
box = mkshapes.makeBox(0.5, 0.5, 0.5, color = [0, 1, 0])
di.addObject(box)

# %%
# %display

# %% [markdown]
# ### Cylinderを作る
# 最初の2つのパラメータはradius(半径)とlength(長さ)。
#
# ```mkshapes.makeCylinder(0.2, 0.6, color = [0, 0, 1])```
#

# %%
cyl = mkshapes.makeCylinder(0.2, 0.6, color = [0, 0, 1])
di.addObject(cyl)

# %%
cyl.translate(fv(0, 1., 0))

# %%
# %display

# %% [markdown]
# ### Sphereを作る
# パラメータはradius(半径)。
#
# ```mkshapes.makeSphere(0.2, color = [1, 0, 0])```

# %%
sph = mkshapes.makeSphere(0.2, color = [1, 0, 0])
di.addObject(sph)

# %%
sph.translate(fv(0, 0, 1.))

# %% [markdown]
# ### Torusを作る
# 最初の2つのパラメータはトーラスの軸の半径と、トーラス全体の円の半径。次の2つのパラメータは、全体の円の開始角度と終了角度。
#
# ```mkshapes.makeTorus(0.3, 0.1, 0, PI, color = [1, 0, 1])```

# %%
trs = mkshapes.makeTorus(0.3, 0.1, 0, PI, color = [1, 0, 1])
di.addObject(trs)

# %%
trs.translate(fv(1., 0, 0))

# %% [markdown]
# ### Coneを作る
# 最初の2つのパラメータはradius(半径)とlength(長さ)。
#
# ```mkshapes.makeCone(0.3, 0.6, color = [1, 1, 0])```

# %%
cone = mkshapes.makeCone(0.3, 0.6, color = [1, 1, 0])
di.addObject(cone)

# %%
cone.translate(fv(0, 0, -1))

# %% [markdown]
# ### 全体表示する

# %%
di.viewAll()

# %%
# %display

# %% [markdown]
# ### ファイルに保存する

# %% [markdown]
# ファイルへの書き出し。<scene_object>は書き出すオブジェクト。
#
# ```di.SgPosTransform``` は ```di``` で表示したオブジェクトです。
#
# ```exportMesh(<filename>, <sene_object>)```

# %%
succ = mkshapes.exportMesh("/userdir/test.obj", di.SgPosTransform) ## all Object

# %% [markdown]
# ### 表示を消す

# %%
di.clear()

# %% [markdown]
# ### メッシュファイルをロードする

# %%
mesh0 = mkshapes.loadMesh('/userdir/test.obj')

# %% [markdown]
# ロードしたメッシュファイルの表示

# %%
di.addObject(mesh0)

# %% [markdown]
# ### メッシュを移動させる

# %%
mesh0.translate(fv(0, 0, 0.5))

# %%
mesh0.rotate(-PI/6, fv(1, 0, 0))

# %%
# %display

# %% [markdown]
# ### 全体表示

# %%
di.viewAll()

# %% [markdown]
# ### カメラ移動の話

# %%
ib.getCameraCoordsParam()

# %% [markdown]
# ib.cameraPositionLookingAt の3つのパラメータは、カメラの位置、カメラの視線（光軸）の先の点、カメラの上方向になります。

# %%
cam_coords = ib.cameraPositionLookingAt([3.0, 1.5, 3.0], [0, 0, 0.1], [0, 0, 1])
cam_coords

# %%
ib.setCameraCoords(cam_coords)

# %%
# %display

# %%
ret = ib.getCameraCoords()

# %%
ret

# %%
di.viewAll()

# %%
ret = ib.getCameraCoordsParam()

# %%
ret['fov'] = 1.2

# %%
ret

# %%
ib.setCameraCoordsParam(ret)

# %%
# %display
