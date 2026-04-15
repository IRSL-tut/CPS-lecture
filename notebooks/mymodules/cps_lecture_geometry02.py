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
# # 幾何構造を作る（その３）

# %%
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

# %%
#表示用オブジェクト
di=DrawInterface()

# %% [markdown]
# ## 直線

# %%
d_lns=mkshapes.makeLines([[0,0,0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]])
di.addObject(d_lns)

# %%
# %display

# %%
di.clear()

# %% [markdown]
# ## 曲線の壁

# %%
points=[]
NN = 36
for idx in range(NN+1):
    xx = 2*PI/NN*idx
    ss = math.sin(xx)
    points.append(fv(xx, ss))

# %%
o_wall = mkshapes.makeLineAlignedWall(points, height=1.0, thickness=0.04)
di.addObject(o_wall)

# %%
# %display

# %%
di.clear()

# %% [markdown]
# ## オブジェクト

# %%
obj0 = mkshapes.makeBasket(0.4, 0.7, 0.3, thickness=0.02, bottom_thickness=0.02)
obj0.translate(fv(1.0, 0, 0))
di.addObject(obj0)

# %%
obj1 = mkshapes.makeTable4Legs(1.2, 0.55, 0.7, thickness=0.05, leg_size=0.1)
obj1.translate(fv(0, -1.0, 0))
di.addObject(obj1)

# %%
obj2 = mkshapes.makeRoundTable(0.4, 0.7, thickness=0.05)
di.addObject(obj2)

# %%
# %display

# %%
## di.clear()

# %% [markdown]
# ## BoundingBox表示

# %%
o_bx = mkshapes.makeBoxFromBoundingBox(obj2.target, line=True)
di.addObject(o_bx)

# %%
# %display
