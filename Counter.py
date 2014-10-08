#define class to count individual letter instances
alist =['a','c','b','q']
blist =['e','d','g','f']
uplist = ['i','h','j','m']
downlist = ['t']
leftlist = ['k','l','o']
rightlist = ['n','s','p']
startlist = ['r','w']
selectlist = ['u','v','y','z','x']
class Counter:
    def __init__(self, string):
        self.string = string
        self.val = 0
        self.d = {}
        self.compare_val = 0
        self.compare_str = ''
        self.button_dict = {}
        self.up = 0
    #define method to count individual letter freq
    def count(self):
        self.d = {}
        alpha = list('abcdefghijklmnopqrstuvwxyz')
        for letter in alpha:
            self.d[letter] = self.string.count(letter)
            
    #define method to get actual letter
    def get_button(self):
        '''#print self.d['t']
        self.up = self.d['t']
        #print self.up
        left = self.d['o']+self.d['r']
        #down = self.d['h']+self.d['i']+self.d['s']
        down = 0
        right = self.d['a']
        b = self.d['k']+self.d['l']+self.d['m']+self.d['n']
        a= self.d['d']+self.d['g']+self.d['j']+self.d['p']+self.d['q']+self.d['v']
        start = self.d['u']+self.d['w']+self.d['x']+self.d['y']+self.d['z']
        select = self.d['b']+self.d['c']+self.d['f']'''
        left = 0
        right = 0
        down = 0
        a = 0
        b = 0
        start = 0
        select = 0
        for let in alist:
            a = a+self.d[let]
        for let in blist:
            b = b+self.d[let]
        for let in uplist:
            self.up = self.up+self.d[let]
        for let in downlist:
            down = down+self.d[let]
        for let in leftlist:
            left = left+self.d[let]
        for let in rightlist:
            right = right+self.d[let]
        for let in startlist:
            start = start+self.d[let]
        for let in selectlist:
            select = select+self.d[let]
        print 'letters assigned'
        self.button_dict={'Up':self.up, 'Left':left, "Down":down, "Right":right, "B":b, "A":a, "Start":start, "Select":select}
        print self.button_dict
        #print self.button_dict
        #start comparing
        compare_val = 0
        compare_str = ''
        for item in self.button_dict:
            if self.button_dict[item] > self.compare_val:
                self.compare_str = item
                self.compare_val = self.button_dict[item]
        return self.compare_str
