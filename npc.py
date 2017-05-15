'''
Created on 4 de abr de 2017

@author: helio
'''

class NPC(object):
    '''
    classdocs
    '''


    def __init__(self, name, init, sheet, hp, des):
        '''
        Constructor
        '''
        self.name, self.init, self.sheet, self.hp, self.des = name, init, sheet, hp, des
        