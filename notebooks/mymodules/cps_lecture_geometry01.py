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
# # 幾何構造を作る（その２）

# %%
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

# %%
#表示用オブジェクト
di=DrawInterface()

# %% [markdown]
# ## 3次元点群

# %%
d_pts=mkshapes.makePoints([[0,0,0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]], colors=[[1,0,0], [0,1,0]], colorIndices=[0,1,0,1,0])
di.addObject(d_pts)

# %%
# %display

# %% [markdown]
# ## Extrusion

# %%
points_on_y_plane=[[-0.22, -0.1], [0.22, -0.1], [0.34,  0.06], [-0.34,  0.06], [-0.22, -0.1]]
d_ext=mkshapes.makeExtrusion(points_on_y_plane, [[ 0, -0.05, 0],  [0, 0.05, 0]], color=[0, 1, 0])
di.addObject(d_ext)

# %%
lst=[]
for pp in points_on_y_plane:
    lst.append([pp[0], -0.05, pp[1]])
    lst.append([pp[0],  0.05, pp[1]])

d_pts1=mkshapes.makePoints(lst)
di.addObject(d_pts1)

# %%
# %display

# %% [markdown]
# ## ElevationGrid

# %%
d_elv0=mkshapes.makeElevationGrid(6, 6, 0.2, 0.2, [0.0]*36, color=[1, 1, 0])
di.addObject(d_elv0)

# %% [markdown]
# もう少し複雑な例

# %%
# %display

# %%
qq=[0., 0, 0, 0, 0, .0,
 0., .1, .1, .1, .1, 0,
 0., .1, .2, .2, .1, 0,
 0., .1, .2, .2, .1, 0,
 0., .1, .1, .1, .1, 0,
 0., 0, 0, 0, 0, 0]
d_elv1=mkshapes.makeElevationGrid(6, 6, 0.2, 0.2, qq, color=[1, 0, 0])
di.addObject(d_elv1)

# %% [markdown]
# 指示したグリッド点の表示

# %%
lst=[]
for z in range(6):
    for x in range(6):
        idx=x + z*6
        lst.append([x*0.2, qq[idx], z*0.2])

d_pts0=mkshapes.makePoints(lst)
di.addObject(d_pts0)

# %%
# %display

# %%
di.clear()

# %% [markdown]
# ## 3次元座標（矢印）

# %%
d_3da=mkshapes.make3DAxis(scale=0.4, coords=coordinates(fv(1.,1.,1.)))
di.addObject(d_3da)

# %%
# %display

# %% [markdown]
# ## 3次元座標（Box）

# %%
d_3db=mkshapes.make3DAxisBox(scale=0.4, coords=coordinates(fv(-1.,1.,1.)))
di.addObject(d_3db)

# %%
di.viewAll()

# %%
# %display

# %% [markdown]
# ## 3次元座標（Line）

# %%
d_cds=mkshapes.makeCoords(length=0.5, lineWidth=4.0, coords=coordinates(fv(-1.,1,0)))
di.addObject(d_cds)

# %%
# %display

# %% [markdown]
# ## 3次元座標（CrossLine）

# %%
d_crs=mkshapes.makeCross(length=0.5, lineWidth=4.0, color=[0.7, 0.5, 0.5], coords=coordinates(fv(-1.,-1.,1.)))
di.addObject(d_crs)

# %%
# %display

# %% [markdown]
# ## テキスト

# %%
d_txt=mkshapes.makeText('IRSL', color=[1, 0, 0])
d_txt.translate(fv(-2.0, 0, 0))
di.addObject(d_txt)

# %%
# %display
