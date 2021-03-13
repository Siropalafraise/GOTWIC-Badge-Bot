import discord
import os
import FichierBadges
from keep_alive import keep_alive

client=discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
     return
  
  if message.content.startswith("!badges help"):
    await message.channel.send("This bot finds the best configuration of badges given the number of grey badges that you have in your inventory and the number of equipments that you want them to be equipped on.\n\nSyntax 1 (normal badges): !badges X Y with X the number of grey badges and Y the number of equipments.\nSyntax 2 (special badges): !badges X Y A B C D E with A-E the bonuses given by the grey-gold badges.\n\nExample 1 (normal badges): !badges 863 8 returns the best configuration of 863 grey badges equipped on 8 equipments.\nExample 2 (special badges): !badges 627 7 1.2 2.25 4.5 9 15 returns the best configuration of 627 grey UC/SOW badges equipped on 7 equipments.\nExample 3 (special badges): !badges 194 6 1.05 1.95 3.9 7.8 13 returns the best configuration of 194 grey CCS/KVK badges equipped on 6 equipments.\n\nGrey = 1\nGreen = 4\nBlue = 16\nPurple = 64\nGold = 256\n\nFor more information, please visit https://github.com/Siropalafraise/GOTWIC-Badge-Bot.")
  
  elif message.content.startswith("!badges"):
    Auteur,_=str(message.author).split("#")
    Liste=message.content.split(" ")

#%% Error checks
    if len(Liste)==3:
      if not Liste[1].isnumeric() or not Liste[2].isnumeric() or not float(Liste[1]).is_integer() or not float(Liste[2]).is_integer() or float(Liste[1])<0 or float(Liste[2])<0:
        await message.channel.send("Error, try again...")
        return
      else:
        BonusGrey=2.0
        BonusGreen=3.75
        BonusBlue=7.5
        BonusPurple=15
        BonusGold=25
    elif len(Liste)==8:
      if not Liste[1].isnumeric() or not Liste[2].isnumeric() or not Liste[3].replace('.','',1).isnumeric() or not Liste[4].replace('.','',1).isnumeric() or not Liste[5].replace('.','',1).isnumeric() or not Liste[6].replace('.','',1).isnumeric() or not Liste[7].replace('.','',1).isnumeric() or not float(Liste[1]).is_integer() or not float(Liste[2]).is_integer() or float(Liste[1])<0 or float(Liste[2])<0 or float(Liste[2])>800 or float(Liste[3])<0 or float(Liste[4])<0 or float(Liste[5])<0 or float(Liste[6])<0 or float(Liste[7])<0 or not (float(Liste[3])<float(Liste[4]) and float(Liste[4])<float(Liste[5]) and float(Liste[5])<float(Liste[6]) and float(Liste[6])<float(Liste[7])):
        await message.channel.send("Error, try again...")
        return
      else:
        BonusGrey=float(Liste[3])
        BonusGreen=float(Liste[4])
        BonusBlue=float(Liste[5])
        BonusPurple=float(Liste[6])
        BonusGold=float(Liste[7])
    else:
      await message.channel.send("Error, try again...")
      return

#%% Best configuration
    NombreGrey=int(Liste[1])
    NombreEquipments=int(Liste[2])
    Matrice=FichierBadges.FonctionBadges(NombreGrey,NombreEquipments,BonusGrey,BonusGreen,BonusBlue,BonusPurple,BonusGold)

#%% Next upgrade
    if NombreGrey<256*NombreEquipments:
      Bonus=Matrice[0,5]
      BonusUpgrade=Matrice[0,5]
      CompteurUpgrade=0
      while BonusUpgrade==Bonus:
        CompteurUpgrade+=1
        MatriceUpgrade=FichierBadges.FonctionBadges(NombreGrey+CompteurUpgrade,NombreEquipments,BonusGrey,BonusGreen,BonusBlue,BonusPurple,BonusGold)
        BonusUpgrade=MatriceUpgrade[0,5]

#%% Special upgrade
    SpecialUpgrade=False
    if NombreEquipments>=1:
      MatriceUpgradeEquipement=FichierBadges.FonctionBadges(NombreGrey,NombreEquipments-1,BonusGrey,BonusGreen,BonusBlue,BonusPurple,BonusGold)
      if MatriceUpgradeEquipement[0,5]==Matrice[0,5]:
        SpecialUpgrade=True

#%% Embed message
    embed = discord.Embed(
      title="Badge report for "+Auteur,
      color=0x00ff00
      )
      
    embed.add_field(name="Best configuration with "+str(NombreGrey)+" grey badges and "+str(NombreEquipments)+" equipments", value=str(int(Matrice[0,0]))+" grey ("+str(BonusGrey)+" %)\n"+str(int(Matrice[0,1]))+" green ("+str(BonusGreen)+" %)\n"+str(int(Matrice[0,2]))+" blue ("+str(BonusBlue)+" %)\n"+str(int(Matrice[0,3]))+" purple ("+str(BonusPurple)+" %)\n"+str(int(Matrice[0,4]))+" gold ("+str(BonusGold)+" %)", inline=False)
    embed.add_field(name="Bonus", value=str(float(Matrice[0,5]))+" %", inline=False)
    if NombreGrey<256*NombreEquipments:
      embed.add_field(name="Next upgrade", value=str(int(CompteurUpgrade))+" more grey badges will boost your bonus to "+str(float(MatriceUpgrade[0,5]))+" % (+ "+str(float(MatriceUpgrade[0,5]-Matrice[0,5]))+" %).\n", inline=False)
    else:
      embed.add_field(name="Next upgrade", value="You have reached the max bonus.", inline=False)
    if SpecialUpgrade:
      embed.add_field(name="Special upgrade", value="You can reach the same bonus with fewer equipments!\nPlease check !badges "+str(NombreGrey)+" "+str(NombreEquipments-1)+".", inline=False)
      embed.set_thumbnail(url="https://i.imgur.com/fclCp7j.gif")
    else:
      embed.set_thumbnail(url="https://i.imgur.com/bJzMtFj.png")
    
    await message.channel.send(embed=embed)

keep_alive()
client.run(os.getenv("Token"))
