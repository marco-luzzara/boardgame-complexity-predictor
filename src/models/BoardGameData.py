from dataclasses import dataclass, asdict
import xml.etree.ElementTree as xe

@dataclass
class BoardGameInfo:
    id: int
    name: str
    numweights: int
    averageweight: float
    playingtime: int
    family: str
    
    @classmethod
    def from_item(cls, item: xe):
        id = item.attrib['id']
        name = item.find('./name[@type=\'primary\']').attrib['value']
        ratings = item.find('./statistics/ratings')
        _playingtime = int(item.find('./playingtime').attrib['value'])
        if _playingtime == 0:
            return None
        return cls(int(id), 
                   name, 
                   numweights=int(ratings.find('./numweights').attrib['value']), 
                   averageweight=float(ratings.find('./averageweight').attrib['value']),
                   playingtime=_playingtime,
                   family=[rank_item.attrib['name'] for rank_item in ratings.findall('./ranks/rank[@type=\'family\']')]
                  )
    
@dataclass
class BoardGame:
    info: BoardGameInfo
    rulebook: str
    
if __name__ == '__main__':
    item = xe.fromstring('''<item type="boardgame" id="10">
<thumbnail>https://cf.geekdo-images.com/Ea4jN5Ko5bPrXrU_AYhhzg__thumb/img/f4FrKXF0HKlPS2jH1AW4_-7Hek8=/fit-in/200x150/filters:strip_icc()/pic1798136.jpg</thumbnail>
<image>https://cf.geekdo-images.com/Ea4jN5Ko5bPrXrU_AYhhzg__original/img/DEi0SFU6mAMZYycGTEJAV4ZBRVw=/0x0/filters:format(jpeg)/pic1798136.jpg</image>
<name type="primary" sortindex="1" value="Elfenland"/>
<name type="alternate" sortindex="1" value="Elfenland (Волшебное Путешествие)"/>
<description>Elfenland is a redesign of the original White Wind game Elfenroads. The game is set in the mythical world of the elves. A group of fledgling elves (the players) are charged with visiting as many of the twenty Elfencities as they can over the course of 4 rounds. To accomplish the task they will use various forms of transportation such as Giant Pigs, Elfcarts, Unicorns, Rafts, Magic Clouds, Trollwagons, and Dragons.&#10;&#10;Gameplay: Players begin in the Elf capitol, draw one face down movement tile, and are dealt eight transport cards and a secret 'home' city card that they must reach at the end of the 4th round or lose points for each city space away from 'home' they are at the end of the game. Markers of each player's color are placed in each city on the board and are collected when the player visits that city (each counts as 1 point).&#10; &#10; The round proceeds in 2 stages. The first part of the round consists of the drawing of Tiles showing the differing types of transport (except rafts) from a combination of face up and face down tiles (if a player doesn't like the 5 tiles that are face up; they can always draw blind from the face down tiles and hope to get one they need). These transport tiles need to match the Transportation cards in your hand to use them most effectively. After each player has a total of 4 tiles they take turns placing a tile on any one of the roads that run between the elf cities. Only one transport tile may be placed on each road; so players may use other players tiles to travel if they have the matching cards in their hand. This frequently causes a readjustment of planned travel routes as other players tiles can allow you to move farther or shorter than you had first thought. Players can play their tiles to help themselves or hinder others by playing a slow mode of transport on another players (perceived) path.&#10;&#10;Each mode of transport has certain terrain it can travel through quickly or slowly, and those that it cannot. These are listed on the top of each transportation card by the number terrain symbols. The number of terrain symbols equals how many matching cards you must play to move across a given tile in a given terrain. For example, a Magic Cloud tile placed in a mountain would take one Magic cloud card to travel across (1 mountain symbol on card means Magic clouds are fast in mountains). If the same tile was placed on a road in forest terrain it would require 2 Magic Cloud cards to travel that route (2 Forest symbols on card means Magic Clouds are slow in Forest). Magic Clouds cannot travel in desert terrain at all (no desert symbols on card). All modes of transport are different and Rafts can be used on rivers or lakes without needing tiles. Rafts go slow upstream (2 raft cards needed) and fast downstream (1 card needed). The small lake requires 1 raft card to travel across and the larger lake requires 2 cards to travel across. Players may keep one unused transport counter and up to 4 Transportation cards from one round to the next.&#10;&#10;The second part of the round begins after all players have finished placing their transportation tiles for the round. Each player plays his cards and moves his elf-boot around the board collecting his tokens from the cities visited. If there is a Transport tile on a route and a player has no matching Transportation card he may 'Caravan' across it by playing any 3 Transportation cards from his hand.&#10;&#10;As a bit of 'take that' each player has a trouble tile which can be placed next to any transportation tile during the first part of the round. This counter means that in order to travel that path an additional card of the transport type must be played or 4 cards to 'Caravan'.&#10;&#10;Victory: if at the end of round 3 a player has visited all 20 cities he is the winner. If not the game ends after round 4 when 'Home' cities are revealed and each player subtracts points for each city he is away from his 'home' subtracting that from his collected city tokens. The person with the highest score wins.&#10;&#10;</description>
<yearpublished value="1998"/>
<minplayers value="2"/>
<maxplayers value="6"/>
<poll name="suggested_numplayers" title="User Suggested Number of Players" totalvotes="108">
<results numplayers="1">
<result value="Best" numvotes="0"/>
<result value="Recommended" numvotes="0"/>
<result value="Not Recommended" numvotes="66"/>
</results>
<results numplayers="2">
<result value="Best" numvotes="2"/>
<result value="Recommended" numvotes="21"/>
<result value="Not Recommended" numvotes="61"/>
</results>
<results numplayers="3">
<result value="Best" numvotes="11"/>
<result value="Recommended" numvotes="51"/>
<result value="Not Recommended" numvotes="20"/>
</results>
<results numplayers="4">
<result value="Best" numvotes="57"/>
<result value="Recommended" numvotes="37"/>
<result value="Not Recommended" numvotes="1"/>
</results>
<results numplayers="5">
<result value="Best" numvotes="39"/>
<result value="Recommended" numvotes="48"/>
<result value="Not Recommended" numvotes="3"/>
</results>
<results numplayers="6">
<result value="Best" numvotes="24"/>
<result value="Recommended" numvotes="52"/>
<result value="Not Recommended" numvotes="15"/>
</results>
<results numplayers="6+">
<result value="Best" numvotes="0"/>
<result value="Recommended" numvotes="2"/>
<result value="Not Recommended" numvotes="52"/>
</results>
</poll>
<playingtime value="60"/>
<minplaytime value="60"/>
<maxplaytime value="60"/>
<minage value="10"/>
<poll name="suggested_playerage" title="User Suggested Player Age" totalvotes="36">
<results>
<result value="2" numvotes="0"/>
<result value="3" numvotes="0"/>
<result value="4" numvotes="0"/>
<result value="5" numvotes="1"/>
<result value="6" numvotes="6"/>
<result value="8" numvotes="18"/>
<result value="10" numvotes="11"/>
<result value="12" numvotes="0"/>
<result value="14" numvotes="0"/>
<result value="16" numvotes="0"/>
<result value="18" numvotes="0"/>
<result value="21 and up" numvotes="0"/>
</results>
</poll>
<poll name="language_dependence" title="Language Dependence" totalvotes="34">
<results>
<result level="36" value="No necessary in-game text" numvotes="34"/>
<result level="37" value="Some necessary text - easily memorized or small crib sheet" numvotes="0"/>
<result level="38" value="Moderate in-game text - needs crib sheet or paste ups" numvotes="0"/>
<result level="39" value="Extensive use of text - massive conversion needed to be playable" numvotes="0"/>
<result level="40" value="Unplayable in another language" numvotes="0"/>
</results>
</poll>
<link type="boardgamecategory" id="1010" value="Fantasy"/>
<link type="boardgamecategory" id="1097" value="Travel"/>
<link type="boardgamemechanic" id="2040" value="Hand Management"/>
<link type="boardgamemechanic" id="2081" value="Network and Route Building"/>
<link type="boardgamemechanic" id="2041" value="Open Drafting"/>
<link type="boardgamemechanic" id="2078" value="Point to Point Movement"/>
<link type="boardgamefamily" id="7005" value="Creatures: Dragons"/>
<link type="boardgamefamily" id="19299" value="Creatures: Fairies / Elves / Pixies"/>
<link type="boardgamefamily" id="68281" value="Creatures: Trolls"/>
<link type="boardgamefamily" id="42078" value="Creatures: Unicorns"/>
<link type="boardgamefamily" id="70360" value="Digital Implementations: Board Game Arena"/>
<link type="boardgamefamily" id="34380" value="Game: Elfenroads"/>
<link type="boardgameexpansion" id="256951" value="Brettspiel Adventskalender 2018"/>
<link type="boardgameexpansion" id="158" value="Elfengold"/>
<link type="boardgameexpansion" id="147542" value="Elfenland: Back to the Roads"/>
<link type="boardgameexpansion" id="122213" value="Elfenland: Der Elfen-Zauberer"/>
<link type="boardgameexpansion" id="264237" value="Elfenland: Favor of the Towns"/>
<link type="boardgameexpansion" id="225880" value="Stadt Land Spielt Limitierte Sonderdrucke 2013"/>
<link type="boardgameimplementation" id="180325" value="Elfenroads"/>
<link type="boardgameimplementation" id="229" value="King of the Elves"/>
<link type="boardgameimplementation" id="711" value="Elfenroads" inbound="true"/>
<link type="boardgamedesigner" id="9" value="Alan R. Moon"/>
<link type="boardgameartist" id="74" value="Doris Matthäus"/>
<link type="boardgameartist" id="9" value="Alan R. Moon"/>
<link type="boardgamepublisher" id="8" value="AMIGO"/>
<link type="boardgamepublisher" id="267" value="999 Games"/>
<link type="boardgamepublisher" id="4304" value="Albi"/>
<link type="boardgamepublisher" id="6818" value="Corfix"/>
<link type="boardgamepublisher" id="18852" value="Hobby World"/>
<link type="boardgamepublisher" id="3395" value="Midgaard Games"/>
<link type="boardgamepublisher" id="3" value="Rio Grande Games"/>
<statistics page="1">
<ratings>
<usersrated value="8580"/>
<average value="6.69069"/>
<bayesaverage value="6.46197"/>
<ranks>
<rank type="subtype" id="1" name="boardgame" friendlyname="Board Game Rank" value="1203" bayesaverage="6.46197"/>
<rank type="family" id="5499" name="familygames" friendlyname="Family Game Rank" value="352" bayesaverage="6.51464"/>
</ranks>
<stddev value="1.25012"/>
<median value="0"/>
<owned value="10530"/>
<trading value="341"/>
<wanting value="167"/>
<wishing value="782"/>
<numcomments value="2218"/>
<numweights value="703"/>
<averageweight value="2.1579"/>
</ratings>
</statistics>
</item>''')
    bg_info = BoardGameInfo.from_item(item)
    bg = BoardGame(bg_info, 'test')
    bg_dict = asdict(bg)
    import pandas as pd
    df = pd.json_normalize([bg_dict])
    print(df)