ó
&k[c           @   sÔ   d  Z  d d l Z d d l m Z m Z d d l m Z m Z d d l m	 Z	 d d l
 Z
 d d l m Z d d l m Z e j   Z e j   d k r¨ e j d  n  d	   Z d
   Z d e f d     YZ d S(   s[   
batch.py 

Class to setup and run batch simulations

Contributors: salvadordura@gmail.com
iÿÿÿÿN(   t   izipt   product(   t   Popent   PIPE(   t   sleep(   t   specs(   t   hi    c         C   s^   d Gt  j   GHd |  | | f } | d GHt | j d  d t d t } | j j   GHd  S(   Ns   
Job in rank id: s"   nrniv %s simConfig=%s netParams=%ss   
t    t   stdoutt   stderr(   t   pct   idR   t   splitR   R   t   read(   t   scriptt   cfgSavePatht   netParamsSavePatht   commandt   proc(    (    s?   /u/salvadord/Documents/ISB/Models/netpyne_repo/netpyne/batch.pyt   runJob   s
    	!c         C   sÔ   t  |   t k rK x» |  D]+ } t  |  t t g k r t |  q q Wn t  |   t k rÐ xp |  j   D]_ \ } } t  |  t t g k r t |  n  t  |  t k rj |  j |  |  t |  <qj qj Wn  |  S(   N(   t   typet   listt   dictt
   tupleToStrt	   iteritemst   tuplet   popt   str(   t   objt   itemt   keyt   val(    (    s?   /u/salvadord/Documents/ISB/Models/netpyne_repo/netpyne/batch.pyR      s    #t   Batchc           B   s;   e  Z d  d d d i  d  Z d   Z d   Z d   Z RS(   s   cfg.pys   netParams.pyc   	      C   sä   d t  t j j    |  _ | |  _ | |  _ | |  _ d |  j |  _ d |  _	 i  |  _
 g  |  _ | r¦ x; | j   D]* \ } } |  j j i | d 6| d 6 qu Wn  | rà x1 |  j D]# } | d | k r¶ t | d <q¶ q¶ Wn  d  S(   Nt   batch_t   /t   gridt   labelt   valuest   group(   R   t   datetimet   datet   todayt
   batchLabelt   cfgFilet   initCfgt   netParamsFilet
   saveFoldert   methodt   runCfgt   paramsR   t   appendt   True(	   t   selfR+   R-   R1   t   groupedParamsR,   t   kt   vt   p(    (    s?   /u/salvadord/Documents/ISB/Models/netpyne_repo/netpyne/batch.pyt   __init__1   s    						% c         C   s  d d  l  } d d l m } | j j |  } | j |  d } | j d  d } y | j |  Wn/ t k
 r | j j |  s d G| GHq n X| |  j	  } i t
 |  d 6} | d k rd d  l }	 d	 | GHt | d
  # }
 |	 j | |
 d d d t Wd  QXn  d  S(   Niÿÿÿÿ(   t   deepcopyi    t   .i   s    Could not createt   batcht   jsons   Saving batch to %s ... t   wt   indenti   t	   sort_keys(   t   ost   copyR:   t   patht   basenameR   t   mkdirt   OSErrort   existst   __dict__R   R=   t   opent   dumpR3   (   R4   t   filenameRA   R:   RD   t   foldert   extt   odictt   dataSaveR=   t   fileObj(    (    s?   /u/salvadord/Documents/ISB/Models/netpyne_repo/netpyne/batch.pyt   saveA   s"    	c         C   s   t  | t  r |  j } xT t t |  d  D]< } t  | t j  r] t | | |  } q/ | | | } q/ W| | | d <n t |  j | |  d  S(   Ni   iÿÿÿÿ(	   t
   isinstanceR   t   cfgt   ranget   lenR   t	   SimConfigt   getattrt   setattr(   R4   t
   paramLabelt   paramValt	   containert   ip(    (    s?   /u/salvadord/Documents/ISB/Models/netpyne_repo/netpyne/batch.pyt   setCfgNestedParamZ   s    	c   8      C   sð
  |  j  dJ k rì
d d  l } d d  l } y | j |  j  Wn5 t k
 rr | j j |  j  ss d G|  j GHqs n X|  j d |  j d } |  j	 |  |  j d |  j d } | j
 d | j j t  d	 |  |  j d |  j d
 } | j
 d |  j d	 |  | j j |  j  j d  d } t j | |  j  } | j |  _ t |  j _ t |  j  d k r x0 |  j j   D] \ } } |  j | |  q}Wn  |  j  d k rt }	 t }
 xI |  j D]> } d | k rêt | d <t }
 qÅ| d t k rÅt }	 qÅqÅW|
 rVt g  |  j D]* } | d t k r| d | d f ^ q  \ } } n dK } dL } t g  |  j D]* } | d t k ro| d | d f ^ qo  \ } } t t |    } t t g  | D] } t t |   ^ qÇ   } |	 r{t g  |  j D]* } | d t k rþ| d | d f ^ qþ  \ } } t  |   } t  g  | D] } t t |   ^ qM  } | | } qdM g } dN g } n  |  j! j" d d   d k rÛx- t t$ t% j&     D] } t% j'   qÄWn  xÖt | |  D]Å\ } } x¶t | |  D]¥\ } } |	 r0| | } | | } n | } | } | G| GHxM t( |  D]? \ } } | | } |  j | |  t) |  d t) |  GHqRW|  j d j* g  | D] } d j* d t) |   ^ q¨ } |  j d | } |  j! j" d t  r| j | d  rd | GHn|  j! j" d t  rJ| j | d  rJd | GHnX|  j! j" d d   r| j | |  j! d  rd | |  j! d f GHn| |  j _+ |  j |  j _ |  j d | d } |  j j	 |  |  j! j" d d   d k rm|  j! j" d d  }  t, |   |  j! j" d  d  }! |  j! j" d! d  }" |  j! j" d" d#  }# |  j! j" d$ d%  }$ |  j! j" d& d'  }% |  j! j" d( d)  }& d* |! |" f }' |  j! j" d+ d  }( |! |" }) d, |$ |) |# | | f }* d- | |% |& |' | | |( |* f }+ d. G| GH|+ d/ GHd0 | }, t- |, d1   }- |- j. d2 |+  Wd  QXt/ d3 |, g d4 t0 d5 t0 }. |. j1 |. j2 }/ }0 n5|  j! j" d d   d6 k r\	|  j! j" d d  }  t, |   |  j! j" d7 d8  }1 |  j! j" d  d  }! |  j! j" d9 d  }2 |  j! j" d: d;  }3 |  j! j" d< d  }4 |  j! j" d" d#  }# |  j! j" d$ d=  }$ |  j! j" d& d'  }% |  j! j" d> d   }5 |  j! j" d+ d  }( |5 rd? |5 }6 n d }6 |! |2 }) d, |$ |) |# | | f }* d@ | |1 |% |! |2 | | |3 |6 |( |4 |* f }+ d. G| GH|+ d/ GHdA | }, t- |, d1   }- |- j. d2 |+  Wd  QXt/ dB |, g dC t0 d5 t0 }. |. j1 |. j2 }/ }0 nF|  j! j" d d   dD k rE
|  j d | } dE G| GH|  j! j" dF d  }7 |  j! j" d< d  }4 |  j! j" d" d#  }# |  j! j" d$ d=  }$ d, |$ |7 |# | | f }* |* d/ GHt/ |* j d	  d5 t- | dG d1  d4 t- | dH d1  }. n] |  j! j" d d   d k r¢
|  j d | } d. G| GHt% j3 t4 |  j! j" d" d#  | |  n  t, d  qWqëWy! x t% j5   rÓ
t, d  qº
WWn n Xt, dI  n  d  S(O   NR#   R   iÿÿÿÿs    Could not createR"   s   _batch.jsons   _batchScript.pys   cp R   s   _netParams.pyR;   i    R&   R$   R%   R   t   mpi_bulletins    = t    t   _t   skips   .jsons3   Skipping job %s since output file already exists...t   skipCfgs	   _cfg.jsons0   Skipping job %s since cfg file already exists...t
   skipCustoms/   Skipping job %s since %s file already exists...t
   hpc_torquet   sleepIntervali   t   nodest   ppnR   s   init.pyt
   mpiCommandt   mpiexect   walltimes   00:30:00t	   queueNamet   defaults   nodes=%d:ppn=%dt   customs9   %s -np %d nrniv -python -mpi %s simConfig=%s netParams=%ss¨   #!/bin/bash 
#PBS -N %s
#PBS -l walltime=%s
#PBS -q %s
#PBS -l %s
#PBS -o %s.run
#PBS -e %s.err
%s
cd $PBS_O_WORKDIR
echo $PBS_O_WORKDIR
%s
                            s   Submitting job s   
s   %s.pbsR>   s   %st   qsubR	   R   t	   hpc_slurmt
   allocationt   csd403t   coresPerNodet   emails   a@b.cRL   t   ibrunt   reservations   #SBATCH --res=%ss  #!/bin/bash 
#SBATCH --job-name=%s
#SBATCH -A %s
#SBATCH -t %s
#SBATCH --nodes=%d
#SBATCH --ntasks-per-node=%d
#SBATCH -o %s.run
#SBATCH -e %s.err
#SBATCH --mail-user=%s
#SBATCH --mail-type=end
%s
%s

source ~/.bashrc
cd %s
%s
wait
                            s	   %s.sbatcht   sbatcht   stdint
   mpi_directs   Running job t   coress   .runs   .erri
   (   R#   R   (    (    (   i    (   i    (6   R/   RA   t   globRE   R.   RF   RC   RG   R*   RQ   t   systemt   realpatht   __file__R-   RD   R+   R   t   impt   load_sourceRS   t   Falset   checkErrorsRU   R,   R   R]   R1   R3   t   zipR   R   RT   R    R0   t   gett   Nonet   intR
   t   nhostt	   runworkert	   enumerateR   t   joint   simLabelR   RI   t   writeR   R   Rw   R   t   submitR   t   working(8   R4   RA   Rz   t
   targetFileR   t   cfgModuleNamet	   cfgModuleRY   RZ   R5   t   ungroupedParamsR8   t	   labelListt
   valuesListt   valueCombinationst   xt   indexCombinationst   labelListGroupt   valuesListGroupt   valueCombGroupst   indexCombGroupst   iworkert   iCombGt   pCombGt   iCombNGt   pCombNGt   iCombt   pCombt   iR   t   jobNameR   Re   Rf   Rg   R   Rh   Rj   Rk   t   nodesppnRm   t   numprocR   t	   jobStringt	   batchfilet	   text_fileR   t   outputt   inputRp   Rr   Rs   RL   Ru   t   resRy   (    (    s?   /u/salvadord/Documents/ISB/Models/netpyne_repo/netpyne/batch.pyt   runf   s   %"
	IF1F+	
	
<((/

"		


.		
		>	(N(   t   __name__t
   __module__R   R9   RQ   R]   R¬   (    (    (    s?   /u/salvadord/Documents/ISB/Models/netpyne_repo/netpyne/batch.pyR    /   s   		(   t   __doc__R'   t	   itertoolsR    R   t
   subprocessR   R   t   timeR   R~   t   netpyneR   t   neuronR   t   ParallelContextR
   R   t   master_works_on_jobsR   R   t   objectR    (    (    (    s?   /u/salvadord/Documents/ISB/Models/netpyne_repo/netpyne/batch.pyt   <module>   s    		