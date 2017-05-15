'''
Created on 14 de mai de 2017

@author: helio
'''
from npc import NPC

def npcDecoder( dataJson ):
    #return NPC(  )
    print dataJson
    return NPC(dataJson['name'], dataJson['init'], dataJson['sheet'], dataJson['hp'], dataJson['des'])
    