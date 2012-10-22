import math
def poscasillas8(maxcasillas):
    a=7*math.sqrt(2)/2
    b=3*math.sqrt(2)/2
    c=3*math.tan(math.pi/8)
    posCasillas=[None]*maxcasillas
    posCasillas[0]=(0, 0, 0)
    posCasillas[1]=(21, 60, 0.7)
    posCasillas[2]=(21, 57, 0.7)
    posCasillas[3]=(21, 54, 0.7)
    posCasillas[4]=(21, 51, 0.7)
    posCasillas[5]=(21, 48, 0.7)
    posCasillas[6]=(21, 45, 0.7)
    posCasillas[7]=(21, 42, 0.7)
    
    posCasillas[8]=(28, 42, 0.7)
    posCasillas[9]=(21, 42,  0.7)
    
    posCasillas[10]=(21-a, 42-a, 0.7)
    posCasillas[11]=(21-a-b, 42-a+b, 0.7)
    posCasillas[12]=(21-a-b*2, 42-a+b*2, 0.7)
    posCasillas[13]=(21-a-b*3, 42-a+b*3, 0.7)
    posCasillas[14]=(21-a-b*4, 42-a+b*4, 0.7)
    posCasillas[15]=(21-a-b*5, 42-a+b*5, 0.7)
    posCasillas[16]=(21-a-b*6, 42-a+b*6, 0.7)
    posCasillas[17]=(21-2*a-b*6, 42-2*a+b*6, 0.7)
    posCasillas[18]=(21-3*a-b*6, 42-3*a+b*6, 0.7)
    posCasillas[19]=(21-3*a-b*5, 42-3*a+b*5, 0.7)
    posCasillas[20]=(21-3*a-b*4, 42-3*a+b*4, 0.7)
    posCasillas[21]=(21-3*a-b*3, 42-3*a+b*3, 0.7)
    posCasillas[22]=(21-3*a-b*2, 42-3*a+b*2, 0.7)
    posCasillas[23]=(21-3*a-b*1, 42-3*a+b*1, 0.7)
    posCasillas[24]=(21-3*a-b*0, 42-3*a+b*0, 0.7)
    
    posCasillas[25]=(posCasillas[24][0]+a, posCasillas[24][1]+7-b, 0.7)
    posCasillas[26]=(posCasillas[24][0], posCasillas[24][1], 0.7)
    
    posCasillas[27]=(posCasillas[24][0], posCasillas[24][1]-7, 0.7)
    posCasillas[28]=(posCasillas[24][0]-1*3, posCasillas[24][1]-7, 0.7)
    posCasillas[29]=(posCasillas[24][0]-2*3, posCasillas[24][1]-7, 0.7)
    posCasillas[30]=(posCasillas[24][0]-3*3, posCasillas[24][1]-7, 0.7)
    posCasillas[31]=(posCasillas[24][0]-4*3, posCasillas[24][1]-7, 0.7)
    posCasillas[32]=(posCasillas[24][0]-5*3, posCasillas[24][1]-7, 0.7)
    posCasillas[33]=(posCasillas[24][0]-6*3, posCasillas[24][1]-7, 0.7)
    posCasillas[34]=(posCasillas[24][0]-6*3, posCasillas[24][1]-7*2, 0.7)
    posCasillas[35]=(posCasillas[24][0]-6*3, posCasillas[24][1]-7*3, 0.7)
    posCasillas[36]=(posCasillas[24][0]-5*3, posCasillas[24][1]-7*3, 0.7)
    posCasillas[37]=(posCasillas[24][0]-4*3, posCasillas[24][1]-7*3, 0.7)
    posCasillas[38]=(posCasillas[24][0]-3*3, posCasillas[24][1]-7*3, 0.7)
    posCasillas[39]=(posCasillas[24][0]-2*3, posCasillas[24][1]-7*3, 0.7)
    posCasillas[40]=(posCasillas[24][0]-1*3, posCasillas[24][1]-7*3, 0.7)
    posCasillas[41]=(posCasillas[24][0]-0*3, posCasillas[24][1]-7*3, 0.7)
    
    posCasillas[42]=(posCasillas[41][0], posCasillas[41][1]+7, 0.7)
    posCasillas[43]=(posCasillas[41][0], posCasillas[41][1], 0.7)
    
    posCasillas[44]=(posCasillas[41][0]+1*a, posCasillas[41][1]-1*a, 0.7)
    posCasillas[45]=(posCasillas[41][0]+1*a-1*b, posCasillas[41][1]-1*a-1*b, 0.7)
    posCasillas[46]=(posCasillas[41][0]+1*a-2*b, posCasillas[41][1]-1*a-2*b, 0.7)
    posCasillas[47]=(posCasillas[41][0]+1*a-3*b, posCasillas[41][1]-1*a-3*b, 0.7)
    posCasillas[48]=(posCasillas[41][0]+1*a-4*b, posCasillas[41][1]-1*a-4*b, 0.7)
    posCasillas[49]=(posCasillas[41][0]+1*a-5*b, posCasillas[41][1]-1*a-5*b, 0.7)
    posCasillas[50]=(posCasillas[41][0]+1*a-6*b, posCasillas[41][1]-1*a-6*b, 0.7)
    posCasillas[51]=(posCasillas[41][0]+2*a-6*b, posCasillas[41][1]-2*a-6*b, 0.7)
    posCasillas[52]=(posCasillas[41][0]+3*a-6*b, posCasillas[41][1]-3*a-6*b, 0.7)
    posCasillas[53]=(posCasillas[41][0]+3*a-5*b, posCasillas[41][1]-3*a-5*b, 0.7)
    posCasillas[54]=(posCasillas[41][0]+3*a-4*b, posCasillas[41][1]-3*a-4*b, 0.7)
    posCasillas[55]=(posCasillas[41][0]+3*a-3*b, posCasillas[41][1]-3*a-3*b, 0.7)
    posCasillas[56]=(posCasillas[41][0]+3*a-2*b, posCasillas[41][1]-3*a-2*b, 0.7)
    posCasillas[57]=(posCasillas[41][0]+3*a-1*b, posCasillas[41][1]-3*a-1*b, 0.7)
    posCasillas[58]=(posCasillas[41][0]+3*a-0*b, posCasillas[41][1]-3*a-0*b, 0.7)
    
    posCasillas[59]=(posCasillas[58][0]-a, posCasillas[58][1]+a, 0.7)
    posCasillas[60]=(posCasillas[58][0], posCasillas[58][1]-0*3, 0.7)
    
    posCasillas[61]=(posCasillas[58][0]+0*7, posCasillas[58][1]-1*3, 0.7)
    posCasillas[62]=(posCasillas[58][0]+0*7, posCasillas[58][1]-2*3, 0.7)
    posCasillas[63]=(posCasillas[58][0]+0*7, posCasillas[58][1]-3*3, 0.7)
    posCasillas[64]=(posCasillas[58][0]+0*7, posCasillas[58][1]-4*3, 0.7)
    posCasillas[65]=(posCasillas[58][0]+0*7, posCasillas[58][1]-5*3, 0.7)
    posCasillas[66]=(posCasillas[58][0]+0*7, posCasillas[58][1]-6*3, 0.7)
    posCasillas[67]=(posCasillas[58][0]+0*7, posCasillas[58][1]-7*3, 0.7)
    posCasillas[68]=(posCasillas[58][0]+1*7, posCasillas[58][1]-7*3, 0.7)
    posCasillas[69]=(posCasillas[58][0]+2*7, posCasillas[58][1]-7*3, 0.7)
    posCasillas[70]=(posCasillas[58][0]+2*7, posCasillas[58][1]-6*3, 0.7)
    posCasillas[71]=(posCasillas[58][0]+2*7, posCasillas[58][1]-5*3, 0.7)
    posCasillas[72]=(posCasillas[58][0]+2*7, posCasillas[58][1]-4*3, 0.7)
    posCasillas[73]=(posCasillas[58][0]+2*7, posCasillas[58][1]-3*3, 0.7)
    posCasillas[74]=(posCasillas[58][0]+2*7, posCasillas[58][1]-2*3, 0.7)
    posCasillas[75]=(posCasillas[58][0]+2*7, posCasillas[58][1]-1*3, 0.7)
    
    posCasillas[76]=(posCasillas[58][0]+2*7, posCasillas[58][1]-0*3, 0.7)
    posCasillas[77]=(posCasillas[76][0]+7, posCasillas[76][1], 0.7)


    posCasillas[78]=(posCasillas[75][0]+7+1*a, posCasillas[75][1]+3+1*a, 0.7)
    posCasillas[79]=(posCasillas[75][0]+7+1*a+1*b, posCasillas[75][1]+3+1*a-1*b, 0.7)
    posCasillas[80]=(posCasillas[75][0]+7+1*a+2*b, posCasillas[75][1]+3+1*a-2*b, 0.7)
    posCasillas[81]=(posCasillas[75][0]+7+1*a+3*b, posCasillas[75][1]+3+1*a-3*b, 0.7)
    posCasillas[82]=(posCasillas[75][0]+7+1*a+4*b, posCasillas[75][1]+3+1*a-4*b, 0.7)
    posCasillas[83]=(posCasillas[75][0]+7+1*a+5*b, posCasillas[75][1]+3+1*a-5*b, 0.7)
    posCasillas[84]=(posCasillas[75][0]+7+1*a+6*b, posCasillas[75][1]+3+1*a-6*b, 0.7)
    posCasillas[85]=(posCasillas[75][0]+7+2*a+6*b, posCasillas[75][1]+3+2*a-6*b, 0.7)
    posCasillas[86]=(posCasillas[75][0]+7+3*a+6*b, posCasillas[75][1]+3+3*a-6*b, 0.7)
    posCasillas[87]=(posCasillas[75][0]+7+3*a+5*b, posCasillas[75][1]+3+3*a-5*b, 0.7)
    posCasillas[88]=(posCasillas[75][0]+7+3*a+4*b, posCasillas[75][1]+3+3*a-4*b, 0.7)
    posCasillas[89]=(posCasillas[75][0]+7+3*a+3*b, posCasillas[75][1]+3+3*a-3*b, 0.7)
    posCasillas[90]=(posCasillas[75][0]+7+3*a+2*b, posCasillas[75][1]+3+3*a-2*b, 0.7)
    posCasillas[91]=(posCasillas[75][0]+7+3*a+1*b, posCasillas[75][1]+3+3*a-1*b, 0.7)
    posCasillas[92]=(posCasillas[75][0]+7+3*a+0*b, posCasillas[75][1]+3+3*a-0*b, 0.7)
    
    posCasillas[93]=(posCasillas[92][0]-a, posCasillas[92][1]-a, 0.7)
    posCasillas[94]=(posCasillas[92][0], posCasillas[92][1], 0.7)
    
    posCasillas[95]=(posCasillas[92][0]+0*3, posCasillas[92][1]+7*1, 0.7)
    posCasillas[96]=(posCasillas[92][0]+1*3, posCasillas[92][1]+7*1, 0.7)
    posCasillas[97]=(posCasillas[92][0]+2*3, posCasillas[92][1]+7*1, 0.7)
    posCasillas[98]=(posCasillas[92][0]+3*3, posCasillas[92][1]+7*1, 0.7)
    posCasillas[99]=(posCasillas[92][0]+4*3, posCasillas[92][1]+7*1, 0.7)
    posCasillas[100]=(posCasillas[92][0]+5*3, posCasillas[92][1]+7*1, 0.7)
    posCasillas[101]=(posCasillas[92][0]+6*3, posCasillas[92][1]+7*1, 0.7)
    posCasillas[102]=(posCasillas[92][0]+6*3, posCasillas[92][1]+7*2, 0.7)
    posCasillas[103]=(posCasillas[92][0]+6*3, posCasillas[92][1]+7*3, 0.7)
    posCasillas[104]=(posCasillas[92][0]+5*3, posCasillas[92][1]+7*3, 0.7)
    posCasillas[105]=(posCasillas[92][0]+4*3, posCasillas[92][1]+7*3, 0.7)
    posCasillas[106]=(posCasillas[92][0]+3*3, posCasillas[92][1]+7*3, 0.7)
    posCasillas[107]=(posCasillas[92][0]+2*3, posCasillas[92][1]+7*3, 0.7)
    posCasillas[108]=(posCasillas[92][0]+1*3, posCasillas[92][1]+7*3, 0.7)
    posCasillas[109]=(posCasillas[92][0]+0*3, posCasillas[92][1]+7*3, 0.7)
    
    posCasillas[110]=(posCasillas[92][0], posCasillas[92][1]+2*7, 0.7)
    posCasillas[111]=(posCasillas[109][0], posCasillas[109][1], 0.7)
    
    posCasillas[112]=(posCasillas[109][0]-1*a+0*b, posCasillas[109][1]+1*a+0*b, 0.7)
    posCasillas[113]=(posCasillas[109][0]-1*a+1*b, posCasillas[109][1]+1*a+1*b, 0.7)
    posCasillas[114]=(posCasillas[109][0]-1*a+2*b, posCasillas[109][1]+1*a+2*b, 0.7)
    posCasillas[115]=(posCasillas[109][0]-1*a+3*b, posCasillas[109][1]+1*a+3*b, 0.7)
    posCasillas[116]=(posCasillas[109][0]-1*a+4*b, posCasillas[109][1]+1*a+4*b, 0.7)
    posCasillas[117]=(posCasillas[109][0]-1*a+5*b, posCasillas[109][1]+1*a+5*b, 0.7)
    posCasillas[118]=(posCasillas[109][0]-1*a+6*b, posCasillas[109][1]+1*a+6*b, 0.7)
    posCasillas[119]=(posCasillas[109][0]-2*a+6*b, posCasillas[109][1]+2*a+6*b, 0.7)
    posCasillas[120]=(posCasillas[109][0]-3*a+6*b, posCasillas[109][1]+3*a+6*b, 0.7)
    posCasillas[121]=(posCasillas[109][0]-3*a+5*b, posCasillas[109][1]+3*a+5*b, 0.7)
    posCasillas[122]=(posCasillas[109][0]-3*a+4*b, posCasillas[109][1]+3*a+4*b, 0.7)
    posCasillas[123]=(posCasillas[109][0]-3*a+3*b, posCasillas[109][1]+3*a+3*b, 0.7)
    posCasillas[124]=(posCasillas[109][0]-3*a+2*b, posCasillas[109][1]+3*a+2*b, 0.7)
    posCasillas[125]=(posCasillas[109][0]-3*a+1*b, posCasillas[109][1]+3*a+1*b, 0.7)
    posCasillas[126]=(posCasillas[109][0]-3*a+0*b, posCasillas[109][1]+3*a+0*b, 0.7)
    
    posCasillas[127]=(posCasillas[109][0]-2*a, posCasillas[109][1]+2*a, 0.7)
    posCasillas[128]=(posCasillas[7][0]+3*7, posCasillas[7][1]+0*3, 0.7)
    
    posCasillas[129]=(posCasillas[7][0]+2*7, posCasillas[7][1]+0*3, 0.7)
    posCasillas[130]=(posCasillas[7][0]+2*7, posCasillas[7][1]+1*3, 0.7)
    posCasillas[131]=(posCasillas[7][0]+2*7, posCasillas[7][1]+2*3, 0.7)
    posCasillas[132]=(posCasillas[7][0]+2*7, posCasillas[7][1]+3*3, 0.7)
    posCasillas[133]=(posCasillas[7][0]+2*7, posCasillas[7][1]+4*3, 0.7)
    posCasillas[134]=(posCasillas[7][0]+2*7, posCasillas[7][1]+5*3, 0.7)
    posCasillas[135]=(posCasillas[7][0]+2*7, posCasillas[7][1]+6*3, 0.7)
    posCasillas[136]=(posCasillas[7][0]+1*7, posCasillas[7][1]+6*3, 0.7)
    
    #Rampa amarilla
    posCasillas[137]=(posCasillas[7][0]+1*7, posCasillas[7][1]+5*3, 0.7)
    posCasillas[138]=(posCasillas[7][0]+1*7, posCasillas[7][1]+4*3, 0.7)
    posCasillas[139]=(posCasillas[7][0]+1*7, posCasillas[7][1]+3*3, 0.7)
    posCasillas[140]=(posCasillas[7][0]+1*7, posCasillas[7][1]+2*3, 0.7)
    posCasillas[141]=(posCasillas[7][0]+1*7, posCasillas[7][1]+1*3, 0.7)
    posCasillas[142]=(posCasillas[7][0]+1*7, posCasillas[7][1]+0*3, 0.7)
    posCasillas[143]=(posCasillas[7][0]+1*7, posCasillas[7][1]-1*3, 0.7)
    posCasillas[144]=(posCasillas[7][0]+3*7-c, posCasillas[7][1]-1*3, 0.7)#Central
    
    #Rampa azul
    posCasillas[145]=(21-2*a-b*5, 42-2*a+b*5, 0.7)
    posCasillas[146]=(21-2*a-b*4, 42-2*a+b*4, 0.7)
    posCasillas[147]=(21-2*a-b*3, 42-2*a+b*3, 0.7)
    posCasillas[148]=(21-2*a-b*2, 42-2*a+b*2, 0.7)
    posCasillas[149]=(21-2*a-b*1, 42-2*a+b*1, 0.7)
    posCasillas[150]=(21-2*a-b*0, 42-2*a+b*0, 0.7)
    posCasillas[151]=(21-2*a+b*1, 42-2*a-b*1, 0.7)
    posCasillas[152]=(posCasillas[7][0]+c, 42-3, 0.7)#Central
    
    #Rampa roja
    posCasillas[153]=(posCasillas[34][0]+1*3, posCasillas[34][1], 0.7)
    posCasillas[154]=(posCasillas[34][0]+2*3, posCasillas[34][1], 0.7)
    posCasillas[155]=(posCasillas[34][0]+3*3, posCasillas[34][1], 0.7)
    posCasillas[156]=(posCasillas[34][0]+4*3, posCasillas[34][1], 0.7)
    posCasillas[157]=(posCasillas[34][0]+5*3, posCasillas[34][1], 0.7)
    posCasillas[158]=(posCasillas[34][0]+6*3, posCasillas[34][1], 0.7)
    posCasillas[159]=(posCasillas[34][0]+7*3, posCasillas[34][1], 0.7)
    posCasillas[160]=(posCasillas[34][0]+7*3, posCasillas[34][1]+2*7-c, 0.7)#Central
    
    #Rampa verde
    posCasillas[161]=(posCasillas[41][0]+2*a-5*b, posCasillas[41][1]-2*a-5*b, 0.7)
    posCasillas[162]=(posCasillas[41][0]+2*a-4*b, posCasillas[41][1]-2*a-4*b, 0.7)
    posCasillas[163]=(posCasillas[41][0]+2*a-3*b, posCasillas[41][1]-2*a-3*b, 0.7)
    posCasillas[164]=(posCasillas[41][0]+2*a-2*b, posCasillas[41][1]-2*a-2*b, 0.7)
    posCasillas[165]=(posCasillas[41][0]+2*a-1*b, posCasillas[41][1]-2*a-1*b, 0.7)
    posCasillas[166]=(posCasillas[41][0]+2*a-0*b, posCasillas[41][1]-2*a-0*b, 0.7)
    posCasillas[167]=(posCasillas[41][0]+2*a+1*b, posCasillas[41][1]-2*a+1*b, 0.7)
    posCasillas[168]=(posCasillas[41][0]+3, posCasillas[42][1]-7+c,  0.7)#Central
    
    #Rampa gris
    posCasillas[169]=(posCasillas[58][0]+1*7, posCasillas[58][1]-6*3, 0.7)
    posCasillas[170]=(posCasillas[58][0]+1*7, posCasillas[58][1]-5*3, 0.7)
    posCasillas[171]=(posCasillas[58][0]+1*7, posCasillas[58][1]-4*3, 0.7)
    posCasillas[172]=(posCasillas[58][0]+1*7, posCasillas[58][1]-3*3, 0.7)
    posCasillas[173]=(posCasillas[58][0]+1*7, posCasillas[58][1]-2*3, 0.7)
    posCasillas[174]=(posCasillas[58][0]+1*7, posCasillas[58][1]-1*3, 0.7)
    posCasillas[175]=(posCasillas[58][0]+1*7, posCasillas[58][1]-0*3, 0.7)
    posCasillas[176]=(posCasillas[58][0]+c, posCasillas[58][1]+3, 0.7)#Central
    
    #Rampa pink
    posCasillas[177]=(posCasillas[75][0]+7+2*a+5*b, posCasillas[75][1]+3+2*a-5*b, 0.7)
    posCasillas[178]=(posCasillas[75][0]+7+2*a+4*b, posCasillas[75][1]+3+2*a-4*b, 0.7)
    posCasillas[179]=(posCasillas[75][0]+7+2*a+3*b, posCasillas[75][1]+3+2*a-3*b, 0.7)
    posCasillas[180]=(posCasillas[75][0]+7+2*a+2*b, posCasillas[75][1]+3+2*a-2*b, 0.7)
    posCasillas[181]=(posCasillas[75][0]+7+2*a+1*b, posCasillas[75][1]+3+2*a-1*b, 0.7)
    posCasillas[182]=(posCasillas[75][0]+7+2*a+0*b, posCasillas[75][1]+3+2*a-0*b, 0.7)
    posCasillas[183]=(posCasillas[75][0]+7+2*a-1*b, posCasillas[75][1]+3+2*a+1*b, 0.7)
    posCasillas[184]=(posCasillas[76][0]+7-c, posCasillas[76][1]+3, 0.7)#Central
    
    #Rampa orange
    posCasillas[185]=(posCasillas[92][0]+5*3, posCasillas[92][1]+7*2, 0.7)
    posCasillas[186]=(posCasillas[92][0]+4*3, posCasillas[92][1]+7*2, 0.7)
    posCasillas[187]=(posCasillas[92][0]+3*3, posCasillas[92][1]+7*2, 0.7)
    posCasillas[188]=(posCasillas[92][0]+2*3, posCasillas[92][1]+7*2, 0.7)
    posCasillas[189]=(posCasillas[92][0]+1*3, posCasillas[92][1]+7*2, 0.7)
    posCasillas[190]=(posCasillas[92][0]+0*3, posCasillas[92][1]+7*2, 0.7)
    posCasillas[191]=(posCasillas[92][0]-1*3, posCasillas[92][1]+7*2, 0.7)
    posCasillas[192]=(posCasillas[92][0]-1*3, posCasillas[92][1]+c, 0.7)#Central
    
    #Rampa cyan
    posCasillas[193]=(posCasillas[109][0]-2*a+5*b, posCasillas[109][1]+2*a+5*b, 0.7)
    posCasillas[194]=(posCasillas[109][0]-2*a+4*b, posCasillas[109][1]+2*a+4*b, 0.7)
    posCasillas[195]=(posCasillas[109][0]-2*a+3*b, posCasillas[109][1]+2*a+3*b, 0.7)
    posCasillas[196]=(posCasillas[109][0]-2*a+2*b, posCasillas[109][1]+2*a+2*b, 0.7)
    posCasillas[197]=(posCasillas[109][0]-2*a+1*b, posCasillas[109][1]+2*a+1*b, 0.7)
    posCasillas[198]=(posCasillas[109][0]-2*a+0*b, posCasillas[109][1]+2*a+0*b, 0.7)
    posCasillas[199]=(posCasillas[109][0]-2*a-1*b, posCasillas[109][1]+2*a-1*b, 0.7)
    posCasillas[200]=(posCasillas[110][0]-3, posCasillas[109][1]-c, 0.7)#Central
    
    #Casillas iniciales
    posCasillas[201]=(-40, -40, 0.7)
    posCasillas[202]=posCasillas[201]
    posCasillas[203]=posCasillas[201]
    posCasillas[204]=posCasillas[201]
    posCasillas[205]=posCasillas[201]
    posCasillas[206]=posCasillas[201]
    posCasillas[207]=posCasillas[201]
    posCasillas[208]=posCasillas[201]
    return posCasillas
