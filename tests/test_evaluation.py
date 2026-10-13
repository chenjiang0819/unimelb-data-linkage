import ast,json,unittest,io,contextlib
from pathlib import Path
from unittest.mock import patch
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.feature_selection import SelectKBest, mutual_info_classif
NB=json.loads((Path(__file__).resolve().parents[1]/'project.ipynb').read_text())
SOURCES=[''.join(c['source']) for c in NB['cells'] if c['cell_type']=='code']
FEATURES=['mcg','gvh','alm','mit','erl','pox','vac','nuc']
namespace=dict(np=np,pd=pd,train_test_split=train_test_split,KMeans=KMeans,SelectKBest=SelectKBest,mutual_info_classif=mutual_info_classif,FEATURES=FEATURES)
for s in SOURCES:
 if 'def prepared_features' in s or 'def clean_prices' in s:
  t=ast.parse(s); t.body=[x for x in t.body if isinstance(x,ast.FunctionDef)];exec(compile(t,'notebook','exec'),namespace)
prepare=namespace['prepared_features']
class EvaluationTests(unittest.TestCase):
 def setUp(self):
  rng=np.random.RandomState(21)
  self.data=pd.DataFrame(rng.rand(120,8),columns=FEATURES)
  self.data['Class']=np.arange(120)%2
  self.data.loc[::9,'mcg']=np.nan
 def test_holdout_features_and_targets_do_not_affect_training(self):
  train,test=train_test_split(self.data,test_size=0.33333,random_state=0)
  changed=self.data.copy();changed.loc[test.index,FEATURES]=10000;changed.loc[test.index,'Class']=1-changed.loc[test.index,'Class']
  for kwargs in [{},{'interactions':True},{'clusters':True},{'clusters':True,'selection':True},{'selection':True}]:
   with self.subTest(kwargs=kwargs):
    a=prepare(self.data,**kwargs);b=prepare(changed,**kwargs)
    pd.testing.assert_frame_equal(a[0],b[0]);pd.testing.assert_series_equal(a[2],b[2])
    self.assertTrue(set(a[0].index).isdisjoint(a[1].index));self.assertEqual(set(a[0].index)|set(a[1].index),set(self.data.index))
 def test_repeat_finite_features_and_no_mutation(self):
  original=self.data.copy();self.data['mit']=0
  for selection in [False,True]:
   a=prepare(self.data,interactions=True,clusters=True,selection=selection);b=prepare(self.data,interactions=True,clusters=True,selection=selection)
   self.assertTrue(np.isfinite(a[0]).all().all());self.assertTrue(np.isfinite(a[1]).all().all());pd.testing.assert_frame_equal(a[0],b[0])
  pd.testing.assert_frame_equal(original.drop(columns='mit'),self.data.drop(columns='mit'))
 def test_numeric_price_contract(self):
  clean=namespace['clean_prices'];result=clean(pd.Series(['10 USD','bad','20',None]))
  self.assertEqual(result.tolist(),[10,15,20,15])
  with self.assertRaises(ValueError):clean(pd.Series(['bad',None]))
 def test_many_to_many_truth_and_candidate_denominator(self):
  frames={'amazon.csv':pd.DataFrame({'idAmazon':['a','b'],'price':[10,20]}),'google.csv':pd.DataFrame({'id':['g1','g2','g3'],'price':['10 USD','10','20']}),'amazon_google_truth.csv':pd.DataFrame({'idAmazon':['a','a','b'],'idGoogleBase':['g1','g2','g3']})}
  source=next(s for s in SOURCES if '#Blocking for efficient' in s)
  scope={'pd':pd,'np':np}
  with patch.object(pd,'read_csv',side_effect=lambda f,**kw:frames[f].copy()),contextlib.redirect_stdout(io.StringIO()):exec(source,scope)
  self.assertEqual(scope['pc'],1);self.assertEqual(scope['rr'],.5);self.assertEqual(scope['truepositive'],3)
if __name__=='__main__':unittest.main()
