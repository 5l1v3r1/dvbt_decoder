# -*- coding: utf-8 -*-

'''
DVB-T parameters, these can be found in ETSI EN 300 744 V1.5.
'''

CONTINUAL_PILOT_CARRIERS = [
                    0,   48,   54,   87,  141,  156,  192,
    		       201,  255,  279,  282,  333,  432,  450,
    		       483,  525,  531,  618,  636,  714,  759,
    		       765,  780,  804,  873,  888,  918,  939,
    		       942,  969,  984, 1050, 1101, 1107, 1110,
    		      1137, 1140, 1146, 1206, 1269, 1323, 1377,
    		      1491, 1683, 1704, 1752, 1758, 1791, 1845,
    		      1860, 1896, 1905, 1959, 1983, 1986, 2037,
    		      2136, 2154, 2187, 2229, 2235, 2322, 2340,
    		      2418, 2463, 2469, 2484, 2508, 2577, 2592,
    		      2622, 2643, 2646, 2673, 2688, 2754, 2805,
    		      2811, 2814, 2841, 2844, 2850, 2910, 2973,
    		      3027, 3081, 3195, 3387, 3408, 3456, 3462,
    		      3495, 3549, 3564, 3600, 3609, 3663, 3687,
    		      3690, 3741, 3840, 3858, 3891, 3933, 3939,
    		      4026, 4044, 4122, 4167, 4173, 4188, 4212,
    		      4281, 4296, 4326, 4347, 4350, 4377, 4392,
    		      4458, 4509, 4515, 4518, 4545, 4548, 4554,
    		      4614, 4677, 4731, 4785, 4899, 5091, 5112,
    		      5160, 5166, 5199, 5253, 5268, 5304, 5313,
    		      5367, 5391, 5394, 5445, 5544, 5562, 5595,
    		      5637, 5643, 5730, 5748, 5826, 5871, 5877,
    		      5892, 5916, 5985, 6000, 6030, 6051, 6054,
    		      6081, 6096, 6162, 6213, 6219, 6222, 6249,
    		      6252, 6258, 6318, 6381, 6435, 6489, 6603,
    		      6795, 6816]
            
TPS_CARRIERS = [
              34,   50,  209,  346,  413,  569,  595,  688,
             790,  901, 1073, 1219, 1262, 1286, 1469, 1594,
            1687, 1738, 1754, 1913, 2050, 2117, 2273, 2299,
            2392, 2494, 2605, 2777, 2923, 2966, 2990, 3173,
            3298, 3391, 3442, 3458, 3617, 3754, 3821, 3977,
            4003, 4096, 4198, 4309, 4481, 4627, 4670, 4694,
            4877, 5002, 5095, 5146, 5162, 5321, 5458, 5525,
            5681, 5707, 5800, 5902, 6013, 6185, 6331, 6374,
            6398, 6581, 6706, 6799]            

GUARD_LENGTH  = 1120
USEFUL_LENGTH = 35840
SYMBOL_LENGTH = USEFUL_LENGTH + GUARD_LENGTH
NUM_CARRIERS = 6817
NUM_DATA_CARRIERS = 6048
NUM_SYMBOLS_FRAME = 68
NUM_FRAMES_SUPER_FRAME = 4
NUM_CONV_STATES = 64
PILOT_2_DATA_AMP = 7*4/3

NUM_BYTES_TP = 204
NUM_BITS_PER_CARRIER = 6
FIFO_UNIT_DELAY = 17
FIFO_STAGES = 12
NUM_TRNSPT_PCKTS_IN_PRBS_PERIOD = 8
PRBS_PERIODD_BYTES = 1503
NUM_RNDM_BYTES_TP = 188           
            
M_MAX = 8192
NUM_CONSTELLATION_POINTS = 64
GRAY_BITS = [[0, 0, 0], [0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0], 
             [1, 1, 1], [1, 0, 1], [1, 0, 0]]
             
N_BPSC = 6 # number of bits per subcarrier
IBS = 126 # interleaving block size    
            
        
