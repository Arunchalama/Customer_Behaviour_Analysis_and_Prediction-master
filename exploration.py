# -*- coding: utf-8 -*-
"""
@author: pjsudharshan
"""
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt

# Read data
orig = pd.read_csv('attributes_report.csv')
tdata = pd.read_csv('company_log_title.csv')
tdata_trunc = tdata.iloc[:, 4:11].copy()  # Getting only days' count values
tdata_false = tdata_trunc[tdata.subscribed_after_free_trial == 0]
tdata_true = tdata_trunc[tdata.subscribed_after_free_trial == 1]

########################Correlation##############################
corr = tdata.iloc[:, 4:12].corr()

plt.figure(figsize=(10, 8))
ax = plt.imshow(
    corr,
    cmap="coolwarm",
    interpolation='nearest'
)
plt.colorbar(ax.colorbar, fraction=0.046, pad=0.04)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('sav_images/corr.svg', transparent=True)
plt.show()

# Continue with the rest of your code using Matplotlib for other plots


#####Subscribed (True) and Not Subscribed (False)#####
tt = tdata_true.apply(pd.Series.value_counts).fillna(0)
tf = tdata_false.apply(pd.Series.value_counts).fillna(0)

####False case####
tf1 = tf.unstack().reset_index()
tf1.columns=["X","Y","Z"]
tf1['X']=pd.Categorical(tf1['X'])
tf1['X']=tf1['X'].cat.codes

fig = plt.figure(figsize=(10, 8))
ax = fig.gca(projection='3d')
surf=ax.plot_trisurf(tf1['Y'], tf1['X'], tf1['Z'], cmap=plt.cm.viridis, linewidth=0.2)
fig.colorbar( surf, shrink=0.5, aspect=5)
ax.view_init(10, 50)
# ax.invert_xaxis()
plt.title('Not Subscribed')
ax.set_xlabel('Login Count')
ax.set_ylabel('Day')
ax.set_zlabel('Customer Count')
plt.tight_layout()
plt.savefig('sav_images/false3d.svg',transparent=True)
plt.show()
#####Animate#####
# for angle in range(280,350,2):
#     ax.view_init(10, angle)
#     filename='images/false'+str(angle)+'.png'
#     plt.savefig(filename, dpi=96)
#     plt.gca()


####True case####
tt1 = tt.unstack().reset_index()
tt1.columns=["X","Y","Z"]
tt1['X']=pd.Categorical(tt1['X'])
tt1['X']=tt1['X'].cat.codes

fig = plt.figure(figsize=(10, 8))
ax = fig.gca(projection='3d')
surf=ax.plot_trisurf(tt1['Y'], tt1['X'], tt1['Z'], cmap=plt.cm.viridis, linewidth=0.2)
fig.colorbar( surf, shrink=0.5, aspect=5)
ax.view_init(10, 50)
# ax.invert_xaxis()
plt.title('Subscribed')
ax.set_xlabel('Login Count')
ax.set_ylabel('Day')
ax.set_zlabel('Customer Count')
plt.tight_layout()
plt.savefig('sav_images/true3d.svg',transparent=True)
plt.show()
#####Animate#####
# for angle in range(210,350,2):
#     ax.view_init(10, angle)
#     filename='images/true'+str(angle)+'.png'
#     plt.savefig(filename, dpi=96)
#     plt.gca()


#############Company Type Subscribe Percent###################
comp_counts = orig.set_index(["company_type"]).subscribed_after_free_trial.rename('Index') \
    .eq(True).groupby(level=[0]).value_counts(True).unstack(fill_value=0).reset_index()
comp_counts.columns=["company_type","Not Subscribed","Subscribed"]
ax = comp_counts.plot(x='company_type', y='Subscribed', colormap='cividis', kind='bar')
fig = ax.get_figure()
fig.tight_layout()
fig.savefig('sav_images/subscribed_percent.svg',transparent=True)

print(tt,"\n",tf,"\n",comp_counts)