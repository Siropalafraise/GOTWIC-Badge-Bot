# GOTWIC Badge Bot
This bot finds the best configuration of badges given the number of grey badges that you have in your inventory and the number of equipments that you want them to be equipped on. It works with normal badges and special badges from events like UC, SOW, CCS and KVK, and any other badges that will be introduced in the future.

## Commands
* ``!badges help`` - returns instructions (syntax and example)
* ``!badges X Y`` - returns the best configuration of badges based on your total number of grey badges X and the number of equipments that you want them to be equipped on Y
* ``!badges X Y a b c d e`` - returns the best configuration of badges based on your total number of grey badges X and the number of equipments that you want them to be equipped on Y and the different bonuses given by the badges: a, b, c, d, e are respectively the bonus given by grey badges, green badges, blue badges, purple badges, gold badges

## Examples
* ``!badges help`` - returns the instructions (syntax and example)
* ``!badges 863 8`` - returns the best configuration of 863 grey badges on 8 equipments
* ``!badges 627 7 1.2 2.25 4.5 9 15`` - returns the best configuration of 627 grey UC/SOW badges on 7 equipments
* ``!badges 194 6 1.05 1.95 3.9 7.8 13`` - returns the best configuration of 194 grey CCS/KVK badges on 6 equipments

## Installation
* [Click here](https://discord.com/api/oauth2/authorize?client_id=812358480392224778&permissions=11264&scope=bot) to add this bot to your Discord server
* This bot also replies to DMs

## Differences between this bot and [pipermatt's bot](https://github.com/pipermatt/badgebot)
There are 2 main differences:
1. This bot takes into account the number of equipments. It becomes useful if you want to equip a badge on 6 items instead of 8, for example if you want to keep some slots for special badges from events. It also tells you if you can have the same bonus with fewer equipments, for example !badges 352 8 gives the same bonus as !badges 352 7 giving you 1 free slot for any other badge.
2. This bot can work with special badges from events like the Crest of Protection badge from UC, the Crest of Vigor badge from SOW, the war badges from CCS and KVK, and any other badges that will be introduced in the future.

|               | Siropalafraise's bot  | [pipermatt's bot](https://github.com/pipermatt/badgebot) |
| :-- | :-: | :-: |
| Language  | Python  | Javascript  |
| Best configuration<br>(normal badges)  | :heavy_check_mark:  | :heavy_check_mark:  |
| Best configuration<br>(special badges)  | :heavy_check_mark:  | :x:  |
| Equipment optimization  | :heavy_check_mark:  | :x:  |
| Total bonus  | :heavy_check_mark:  | :heavy_check_mark:  |
| Next upgrade  | :heavy_check_mark:  | :heavy_check_mark:  |
| DMs  | :heavy_check_mark:  | :heavy_check_mark:  |

## Contact
For any idea, suggestion, fix, etc., please contact me on Discord (Siropalafraise#3862) or in the game (Sirop)
