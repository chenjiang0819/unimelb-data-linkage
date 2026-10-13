"""Execute the original notebook from a fresh, project-local Python kernel."""
from pathlib import Path
import os,sys,json,subprocess
ROOT=Path(__file__).resolve().parent
build=ROOT/'.build';build.mkdir(exist_ok=True)
for key,folder in [('JUPYTER_DATA_DIR','jupyter-data'),('JUPYTER_RUNTIME_DIR','jupyter-runtime'),('IPYTHONDIR','ipython'),('MPLCONFIGDIR','matplotlib'),('TMPDIR','tmp')]:
    path=build/folder;path.mkdir(exist_ok=True);os.environ[key]=str(path)
os.environ.update(MPLBACKEND='Agg',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
kernel=build/'jupyter-data/kernels/project-check';kernel.mkdir(parents=True,exist_ok=True)
(kernel/'kernel.json').write_text(json.dumps({'argv':[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'],'display_name':'Project check','language':'python'}))
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
p=ROOT/'project.ipynb'
nb=nbformat.read(p,as_version=4)
for cell in nb.cells:
    if cell.cell_type=='code':cell.outputs=[];cell.execution_count=None
nbformat.validate(nb)
NotebookClient(nb,timeout=180,kernel_name='project-check',resources={'metadata':{'path':str(ROOT)}}).execute()
nb.metadata.kernelspec={'display_name':'Python 3','language':'python','name':'python3'}
nbformat.write(nb,build/'executed.ipynb')
html,_=HTMLExporter().from_notebook_node(nb);(build/'executed.html').write_text(html)
print('Clean-kernel execution passed:',sum(c.cell_type=='code' for c in nb.cells),'code cells; artifacts in .build/')

subprocess.run([sys.executable,'-B','-m','unittest','discover','-s','tests','-v'],cwd=ROOT,check=True)
