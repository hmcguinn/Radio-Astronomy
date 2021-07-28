import virgo
from datetime import datetime
from subprocess import Popen

try:

    prefix = './Observations/' + datetime.today().strftime('%Y-%m-%d-%H-%M')  + '/'
    print(prefix)
    cmd = 'mkdir -p ' + prefix
    p = Popen(cmd, shell=True)

    obs = {
        'dev_args': 'rtl,bias=1',
        'rf_gain': 30,
        'if_gain': 25,
        'bb_gain': 18,
        'frequency': 1420e6,
        'bandwidth': 2.4e6,
        'channels': 2048,
        't_sample': 1,
        'duration': 60
    }

    # Calibrate the data 
    print("Calibrating the dish, duration: " + str(obs['duration']) + ' seconds' )
    timestamp = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    cal_file_name = str(prefix + 'cal-' + timestamp + '.dat')
    print("Saving in file: " + cal_file_name)
    print('')
    print('')
    
    #virgo.observe(obs_parameters=obs, obs_file=cal_file_name)
    print('')
    #input("Move the satellite dish to the Galactic Plane")
    print('')
    # Observe 
    obs['duration'] = 120
    print("Starting observation, duration: " + str(obs['duration']) + ' seconds')
    timestamp = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    obs_file_name = str(prefix+ 'observe-' + timestamp + '.dat')
    print("Saving in file: " + obs_file_name)
    print('')
    print('')

    print("Observing")
    virgo.observe(obs_parameters=obs, obs_file=obs_file_name)
    cal_file_name = "cal.dat"
    virgo.plot(obs_parameters=obs, n=20, m=35, f_rest=1420.4057517667e6,
               obs_file=obs_file_name, cal_file=cal_file_name,
               dB=True,  plot_file=prefix+'plot.png')
except Exception as e:
    print(e)
finally:
    pass
    # p = Popen('bias_tee_off.bat', cwd=r'./',shell=True)
    # stdout, stderr = p.communicate()

