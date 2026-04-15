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
# # 連結座標系

# %%
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

# %%
di = DrawInterface()

# %%
di.clear()

# %% [markdown]
# ## 座標系の作成

# %%
cds1 = mkshapes.makeCoords(coords=coordinates(fv(0, 0, 0.)), length=0.2, lineWidth=5)
di.addObject(cds1)

# %%
cds2 = mkshapes.makeCoords(coords=coordinates(fv(0, 0, .5)), length=0.2, lineWidth=5)
di.addObject(cds2)

# %%
cds3 = mkshapes.makeCoords(coords=coordinates(fv(0, 0, 1.)), length=0.2, lineWidth=5)
di.addObject(cds3)

# %%
# %display

# %% [markdown]
# ## 座標系の移動

# %%
cds1.translate(fv(0, -0.5, 0))

# %%
cds3.translate(fv(0, 0.5, 0))

# %%
# %display

# %% [markdown]
# ## 座標系の連結

# %%
cds1.assoc(cds2)
cds2.assoc(cds3)

# %% [markdown]
# ### 連結後の移動

# %%
cds1.translate(fv(-0.5, 0, 0))

# %%
# %display

# %%
cds2.rotate(0.7, coordinates.X)

# %%
# %display

# %% [markdown]
# ### 移動後の座標確認

# %%
cds2.transformation(cds3)

# %% [markdown]
# # ロボットリンクとの対比

# %%
di.clear()

# %% [markdown]
# ## リンクの作成

# %%
ax0 = mkshapes.makeCoords(length=0.25, lineWidth=4)
bx0 = mkshapes.makeBox(0.1, 0.1, 0.5)
bx0.translate(fv(0, 0, 0.25))
ax0.assoc(bx0)
di.addObjects((ax0, bx0))

# %%
ax1 = mkshapes.makeCoords(length=0.25, lineWidth=4)
bx1 = mkshapes.makeBox(0.1, 0.1, 0.5)
bx1.translate(fv(0, 0, 0.25))
ax1.assoc(bx1)
di.addObjects((ax1, bx1))

# %%
ax2 = mkshapes.makeCoords(length=0.25, lineWidth=4)
bx2 = mkshapes.makeBox(0.1, 0.1, 0.5)
bx2.translate(fv(0, 0, 0.25))
ax2.assoc(bx2)
di.addObjects((ax2, bx2))

# %%
ee = mkshapes.makeCoords(length=0.3, lineWidth=6)
di.addObject(ee)

# %% [markdown]
# ## リンクの配置

# %%
ax1.translate(fv(0, 0, 0.5))
ax2.translate(fv(0, 0, 1.0))
ee.translate(fv(0, 0, 1.5))

# %%
# %display

# %% [markdown]
# ## リンクの連結

# %%
bx0.assoc(ax1)
bx1.assoc(ax2)
bx2.assoc(ee)

# %% [markdown]
# ## リンクの移動

# %%
ax0.translate(fv(0, -0.5, 0))

# %%
ax1.rotate(-0.8, coordinates.X)

# %%
ax2.rotate(0.8, coordinates.Y)

# %%
# %display

# %% [markdown]
# ### エンドエフェクタの座標

# %%
ee
