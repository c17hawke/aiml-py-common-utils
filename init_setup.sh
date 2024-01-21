echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python <PYTHON_VERSION>"
conda create --prefix ./env python=<PYTHON_VERSION> -y
echo [$(date)]: "activate env"
source activate ./env
echo [$(date)]: "intalling dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"
