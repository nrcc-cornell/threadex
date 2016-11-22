kill `cat thrdx_run.pid`
rm thrdx_err.log
rm thrdx_run.log
python run_threadex.py -p 4005  -l thrdx_run.log -P thrdx_run.pid 
ls -l thrdx_run.log