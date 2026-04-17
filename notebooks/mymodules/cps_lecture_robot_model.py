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
# # ロボットモデルの使い方

# %%
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

# %% [markdown]
# ## IRSLのRobotModelクラスの使い方
# こちらを主に使って下さい。
#
# irsl_choreonoid.robot_util.RobotModelWrapped クラスになります。
#
# クラス定義
# https://irsl-tut.github.io/irsl_documents/ja/module_irsl_choreonoid.html#irsl_choreonoid.robot_util.RobotModelWrapped

# %%
fname = iu.parseURL('choreonoid://share/model/HRP4C/HRP4C.body')
if iu.isInChoreonoid():
    robot = RobotModel.loadModelItem(fname, world=False) ## in choreonoid GUI
else:
    robot = RobotModel.loadModel(fname) ## without GUI

# %% [markdown]
# ## Link名とJoint名

# %%
for idx, lk in enumerate(robot.robot.links):
    print('link {}: {}'.format(idx, lk.name))
for idx, j in enumerate(robot.robot.joints):
    print('joint {}: {}'.format(idx, j.jointName))

# %% [markdown]
# ### オブジェクトを作る

# %%
# %display

# %% [markdown]
# ### リンクのリスト

# %%
robot.linkList

# %%
robot.linkNames

# %% [markdown]
# ### jointのリスト

# %%
robot.jointList

# %%
robot.jointNames

# %% [markdown]
# ### デバイス（センサー）のリスト

# %%
robot.deviceList

# %%
robot.deviceNames

# %% [markdown]
# ### angle-vector
# 全身の関節角度のベクトル

# %%
vec = robot.angleVector()
vec

# %% [markdown]
# angle-vectorをセットする

# %%
vec[2] = -0.3
robot.angleVector(vec)

# %% [markdown]
# ### 関節への名前アクセス

# %%
robot.jointAngle('L_HIP_P')

# %%
robot.jointAngle('L_HIP_P', 0.0)

# %% [markdown]
# ### 関節への辞書型でのアクセス

# %%
robot.setAngleMap({'R_HIP_P': -0.8, 'R_KNEE_P': 1.6})

# %%
# %display

# %% [markdown]
# ### ロボットの座標系
# ロボットの座標系は上部をZ軸とし、前方をX軸とする。
#
# ワールド座標系は、Z軸方向が鉛直上向きとする。

# %%
robot.rootCoords()

# %%
cds = coordinates(fv(0, 0, 1.0))
robot.rootCoords(cds)

# %% [markdown]
# ### 四肢(limb), 効果器(EndEffector), 関節グループ
# 関節のまとまりで、先端にエンドエフェクターを持つものを定義する。
#
# これを便宜上、四肢(limb)と名づける。
#
# 名前は自由だが、arm, rarm, larm, rleg, lleg, neck, torso はアクセサが準備されている。

# %%
robot.registerEndEffector('larm', ## end-effector
                          'L_WRIST_R', ## tip-link
                          tip_link_to_eef=coordinates(fv(0, 0, -0.08), fv(0, 0.7071067811865476, 0, 0.7071067811865476)),
                          joint_tuples = (('L_SHOULDER_P', 'shoulder-p'),
                                          ('L_SHOULDER_R', 'shoulder-r'),
                                          ('L_SHOULDER_Y', 'shoulder-y'),
                                          ('L_ELBOW_P', 'elbow-p'),
                                          ('L_WRIST_Y', 'wrist-y'),
                                          ('L_WRIST_R', 'wrist-r'),
                                          )
                          )
robot.registerEndEffector('rarm', ## end-effector
                          'R_WRIST_R', ## tip-link
                          tip_link_to_eef=coordinates(fv(0, 0, -0.08), fv(0, 0.7071067811865476, 0, 0.7071067811865476)),
                          joint_tuples = (('R_SHOULDER_P', 'shoulder-p'),
                                          ('R_SHOULDER_R', 'shoulder-r'),
                                          ('R_SHOULDER_Y', 'shoulder-y'),
                                          ('R_ELBOW_P', 'elbow-p'),
                                          ('R_WRIST_Y', 'wrist-y'),
                                          ('R_WRIST_R', 'wrist-r'),
                                          )
                          )

# %%
robot.larm

# %% [markdown]
# #### limbのangle-vector

# %%
lvec = robot.larm.angleVector()
lvec

# %%
lvec[0] = -0.4
robot.larm.angleVector(lvec)

# %% [markdown]
# #### limbの名前アクセス
#

# %% [markdown]
# ジョイント名

# %%
robot.larm.jointNames

# %% [markdown]
# ニックネームを付けることができる

# %%
robot.larm.renameMap

# %% [markdown]
# 関節への名前アクセス等はモデル全体と同じようにできる

# %%
robot.larm.jointAngle('shoulder-p')

# %%
robot.larm.setAngleMap({'shoulder-p': 0.4, 'elbow-p': -0.8})

# %%
robot.rarm.setAngleMap({'shoulder-p': 0.4, 'elbow-p': -0.8})

# %%
# %display

# %% [markdown]
# #### 手先効果器(EndEffector)

# %%
robot.larm.angleVector(fv(0.2, 0.2, 0, -0.4, 0.2, 0, 0))

# %%
robot.larm.endEffector

# %%
di = DrawInterface()

# %%
cds=mkshapes.makeCoords(coords=robot.larm.endEffector, length=0.14, lineWidth=5)

# %%
robot.assoc(cds, robot.larm.tipLink)

# %%
di.addObject(cds)

# %%
# %display

# %% [markdown]
# #### 逆運動学

# %%
tgt=mkshapes.makeCoords(coords=robot.larm.endEffector, length=0.2, lineWidth=3)

# %%
di.addObject(tgt)

# %%
### 相対的に動かす constraintは拘束する自由度を選択
robot.larm.move(fv(0.0, 0.0, 0.06), constraint='xyz')

# %%
robot.larm.inverseKinematics(tgt)

# %% [markdown]
# ターゲットを動かしてみる

# %%
tgt.translate(fv(0, 0., 0.05), coordinates.wrt.world)

# %%
robot.larm.inverseKinematics(tgt, addNoise=0.5, constraint='xyzRPY')

# %%
cds.newcoords(robot.larm.endEffector)

# %% [markdown]
# ### 名前付きのポーズの設定

# %%
robot.registerNamedPose('default',
                        [0, 0, 0, 0, 0, 0, 0, ## LLEG
                         0, 0, 0, 0, 0, 0, 0, ## RLEG
                         0, 0, 0, ## CHEST
                         0, 0, 0, ## NECK
                         0, 0, 0, 0, 0, 0, ## LARM
                         0, 0, 0, 0, 0, 0, ## RARM
                         ])

# %% [markdown]
# DefaultPoseの呼び出し ```m.setNamedPose('default')``` と同じ

# %%
robot.setDefaultPose()

# %% [markdown]
# 座標系も設定できる

# %%
robot.registerNamedPose

# %%
robot.registerNamedPose('pose0',
                        angles = [0, 0, -0.5, 1.0, -.5, 0, 0, ## LLEG
                                 0, 0, -0.5, 1.0, -0.5, 0, 0, ## RLEG
                                 0, 0, 0, ## CHEST
                                 0, 0, 0, ## NECK
                                 0, 0, 0, 0, 0, 0, ## LARM
                                 0, 0, 0, 0, 0, 0, ## RARM
                                 ],
			            root_coords = coordinates(fv(0, 0, 0.68)))

# %%
robot.setNamedPose('pose0')


# %% [markdown]
# ## ロボットの独自クラスを作る

# %%
class HRP4CModel(RobotModel):
    def __init__(self, robot=None):
        if robot is None:
            fname = iu.parseURL('choreonoid://share/model/HRP4C/HRP4C.body')
            if iu.isInChoreonoid():
                robot = ib.loadRobotItem(fname, world=False)
            else:
                robot = iu.loadRobot(fname)
        super().__init__(robot)
        self.registerEndEffector('larm', ## end-effector
                          'L_WRIST_R', ## tip-link
                          tip_link_to_eef=coordinates(fv(0, 0, -0.08), fv(0, 0.7071067811865476, 0, 0.7071067811865476)),
                          joint_tuples = (('L_SHOULDER_P', 'shoulder-p'),
                                          ('L_SHOULDER_R', 'shoulder-r'),
                                          ('L_SHOULDER_Y', 'shoulder-y'),
                                          ('L_ELBOW_P', 'elbow-p'),
                                          ('L_WRIST_Y', 'wrist-y'),
                                          ('L_WRIST_R', 'wrist-r'),
                                          )
                          )
        self.registerEndEffector('rarm', ## end-effector
                          'R_WRIST_R', ## tip-link
                          tip_link_to_eef=coordinates(fv(0, 0, -0.08), fv(0, 0.7071067811865476, 0, 0.7071067811865476)),
                          joint_tuples = (('R_SHOULDER_P', 'shoulder-p'),
                                          ('R_SHOULDER_R', 'shoulder-r'),
                                          ('R_SHOULDER_Y', 'shoulder-y'),
                                          ('R_ELBOW_P', 'elbow-p'),
                                          ('R_WRIST_Y', 'wrist-y'),
                                          ('R_WRIST_R', 'wrist-r'),
                                          )
                          )
        self.registerEndEffector('lleg', ## end-effector
                                 'L_ANKLE_R', ## tip-link
                                 tip_link_to_eef = coordinates(fv(0, 0, -0.092849)),
                                 joint_tuples = (('L_HIP_Y', 'hip-y'),
                                                 ('L_HIP_R', 'hip-r'),
                                                 ('L_HIP_P', 'hip-p'),
                                                 ('L_KNEE_P' ,'knee-p'),
                                                 ('L_ANKLE_P','ankle-p'),
                                                 ('L_ANKLE_R','ankle-r'),
                                                 )
                                 )
        self.registerEndEffector('rleg', ## end-effector
                                 'R_ANKLE_R', ## tip-link
                                 tip_link_to_eef = coordinates(fv(0, 0, -0.092849)),
                                 joint_tuples = (('R_HIP_Y', 'hip-y'),
                                                 ('R_HIP_R', 'hip-r'),
                                                 ('R_HIP_P', 'hip-p'),
                                                 ('R_KNEE_P' ,'knee-p'),
                                                 ('R_ANKLE_P','ankle-p'),
                                                 ('R_ANKLE_R','ankle-r'),
                                                 )
                                 )
        self.registerNamedPose('default',
                               [0, 0, 0, 0, 0, 0, 0, ## LLEG
                                0, 0, 0, 0, 0, 0, 0, ## RLEG
                                0, 0, 0, ## CHEST
                                0, 0, 0, ## NECK
                                0, 0, 0, 0, 0, 0, ## LARM
                                0, 0, 0, 0, 0, 0, ## RARM
                                ])
        robot.registerNamedPose('pose0',
                        angles = [0, 0, -0.5, 1.0, -.5, 0, 0, ## LLEG
                                 0, 0, -0.5, 1.0, -0.5, 0, 0, ## RLEG
                                 0, 0, 0, ## CHEST
                                 0, 0, 0, ## NECK
                                 0, 0, 0, 0, 0, 0, ## LARM
                                 0, 0, 0, 0, 0, 0, ## RARM
                                 ],
                        root_coords = coordinates(fv(0, 0, 0.68)))
        self.setDefaultPose()


# %% [markdown]
# まえに表示したモデルは消しておく

# %%
robot = HRP4CModel()

# %%
robot.lleg.endEffector

# %% [markdown]
# ### 足先エンドエフェクタを座標に一致させる

# %%
robot.fixLegToCoords(coordinates())

# %%
robot.rleg.setAngleMap({'hip-p': -0.6, 'knee-p': 1.2, 'ankle-p': -0.6})
robot.lleg.setAngleMap({'hip-p': -0.6, 'knee-p': 1.2, 'ankle-p': -0.6})

# %%
# %display

# %%
robot.fixLegToCoords(coordinates())

# %%
# %display

# %% [markdown]
# ### 重心の移動

# %%
robot.rleg.move(fv(0.15, 0, 0))
robot.lleg.move(fv(0.15, 0, 0))

# %%
# %display

# %%
robot.fixLegToCoords(coordinates())

# %%
# %display

# %%
robot.moveCentroidOnFoot() ## 重心を両足の中心にする


# %%
# %display

# %% [markdown]
# ### 重心IK
# under construction

# %% [markdown]
# ### 全身IK
# under construction

# %% [markdown]
# # ジョイント名の表示

# %%
def makePlane(origin):
    cds, fov = ib.getCameraCoords()
    vc = cds.pos - origin
    coordinates.normalizeVector(vc)
    pc_z = vc
    pc_x = np.cross(pc_z, cds.y_axis)
    coordinates.normalizeVector(pc_x)
    pc_y = np.cross(pc_z, pc_x)
    ## axis
    #ax = mkshapes.makeLineAxis(origin, origin+pc_x, colors=[1, 0, 0])
    #ay = mkshapes.makeLineAxis(origin, origin+pc_y, colors=[0, 1, 0])
    #az = mkshapes.makeLineAxis(origin, origin+pc_z, colors=[0, 0, 1])
    ##
    rot=np.column_stack((pc_x, pc_y, pc_z))
    newc = coordinates(origin, rot)
    return newc


# %%
def drawJoint(joint, x_offset=0.25, y_offset=0.0, z_offset=0.12, textHeight=0.14):
    jplane = makePlane(joint.p)
    p_from = jplane.transform_vector(fv(       0,        0, z_offset))
    p_to   = jplane.transform_vector(fv(x_offset, y_offset, z_offset))
    tx = mkshapes.makeText(joint.jointName, textHeight=textHeight)
    ln = mkshapes.makeLineAxis(p_to, p_from, axis_length=0.05, lineWidth=2.0)
    tx.newcoords(jplane)
    tx.translate(fv(x_offset, y_offset, z_offset))
    di.addObjects((ln, tx))


# %%
di.clear()

# %%
drawJoint(robot.jointList[2], y_offset=-0.2)
drawJoint(robot.jointList[3], y_offset=-0.2)
drawJoint(robot.jointList[4], y_offset=-0.2)

# %%
# %display

# %%
#drawJoint(robot.jointList[14], y_offset=0)
#drawJoint(robot.jointList[17], y_offset=0)

# %%
drawJoint(robot.jointList[20], y_offset=+0.2)
drawJoint(robot.jointList[23], y_offset=+0.2)
drawJoint(robot.jointList[25], y_offset=+0.2)

# %%
# %display
