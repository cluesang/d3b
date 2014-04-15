#Initialize

import sqlite3
import ast
import html5lib
import os
from HTMLParser import HTMLParser

#Connect to database in current directory (database must be downloaded elsewhere and placed in current directory)

conn = sqlite3.connect('dnd.sqlite')
c = conn.cursor()
conn.text_factory = str

#table_container = ['dnd_characterclass', 'dnd_characterclassvariant', 'dnd_characterclassvariant_class_skills', 'dnd_characterclassvariantrequiresfeat', 'dnd_characterclassvariantrequiresrace', 'dnd_characterclassvariantrequiresskill', 'dnd_deity', 'dnd_dndedition', 'dnd_domain', 'dnd_domainvariant', 'dnd_domainvariant_deities', 'dnd_feat', 'dnd_feat_feat_categories', 'dnd_featcategory', 'dnd_featrequiresfeat', 'dnd_featrequiresskill', 'dnd_featspecialfeatprerequisite', 'dnd_item', 'dnd_item_aura_schools', 'dnd_item_required_feats', 'dnd_item_required_spells', 'dnd_itemactivationtype', 'dnd_itemauratype', 'dnd_itemproperty', 'dnd_itemslot', 'dnd_language', 'dnd_monster', 'dnd_monster_subtypes', 'dnd_monsterhasfeat', 'dnd_monsterhasskill', 'dnd_monsterspeed', 'dnd_monstersubtype', 'dnd_monstertype', 'dnd_newsentry', 'dnd_race', 'dnd_race_automatic_languages', 'dnd_race_bonus_languages', 'dnd_racefavoredcharacterclass', 'dnd_racesize', 'dnd_racespeed', 'dnd_racespeedtype', 'dnd_racetype', 'dnd_rule', 'dnd_rulebook', 'dnd_skill', 'dnd_skillvariant', 'dnd_specialfeatprerequisite', 'dnd_spell', 'dnd_spell_descriptors', 'dnd_spellclasslevel', 'dnd_spelldescriptor', 'dnd_spelldomainlevel', 'dnd_spellschool', 'dnd_spellsubschool', 'dnd_staticpage', 'dnd_textfeatprerequisite', 'dnd_rules_conditions']

#Page call functions
		
def get_spell(i):
	print '\n'
	print c.execute("SELECT name FROM dnd_spell WHERE id=?", (i,)).fetchall()
	print '-----------------------'
	print "Rulebook: ", c.execute("SELECT dnd_rulebook.name FROM dnd_spell JOIN dnd_rulebook ON dnd_spell.rulebook_id = dnd_rulebook.id WHERE dnd_spell.id =?", (i,)).fetchall()
	print "School: ", c.execute("SELECT dnd_spellschool.name FROM dnd_spell JOIN dnd_spellschool ON dnd_spell.school_id = dnd_spellschool.id WHERE dnd_spell.id =?", (i,)).fetchall()
	print "Descriptor: ", c.execute("SELECT dnd_spelldescriptor.name FROM dnd_spell_descriptors JOIN dnd_spell ON dnd_spell_descriptors.spell_id = dnd_spell.id JOIN dnd_spelldescriptor ON dnd_spell_descriptors.spelldescriptor_id = dnd_spelldescriptor.id WHERE dnd_spell.id =?", (i,)).fetchall()
	print '\n'
	'''if f['dnd_spell']['sub_school_id'].ix[i] == 'NaN':
		pass
	else:
		print f['dnd_spellsubschool']['name'].ix[f['dnd_spell']['sub_school_id'].ix[i]]'''
	print c.execute("SELECT dnd_characterclass.name, dnd_spellclasslevel.level FROM dnd_spellclasslevel LEFT JOIN dnd_spell ON dnd_spellclasslevel.spell_id = dnd_spell.id LEFT JOIN dnd_characterclass ON dnd_spellclasslevel.character_class_id = dnd_characterclass.id WHERE dnd_spell.id =?", (i,)).fetchall()
	print c.execute("SELECT dnd_domain.name, dnd_spelldomainlevel.level FROM dnd_spelldomainlevel LEFT JOIN dnd_spell ON dnd_spelldomainlevel.spell_id = dnd_spell.id LEFT JOIN dnd_domain ON dnd_spelldomainlevel.domain_id = dnd_domain.id WHERE dnd_spell.id =?", (i,)).fetchall()
	print '\n'		
	print "Casting Time: ", c.execute("SELECT casting_time FROM dnd_spell WHERE id=?", (i,)).fetchall()
	print "Range: ", c.execute("SELECT range FROM dnd_spell WHERE id=?", (i,)).fetchall()
	print "Target: ", c.execute("SELECT target FROM dnd_spell WHERE id=?", (i,)).fetchall()
	print "Effect: ", c.execute("SELECT effect FROM dnd_spell WHERE id=?", (i,)).fetchall()
	print "Area: ", c.execute("SELECT area FROM dnd_spell WHERE id=?", (i,)).fetchall()
	print "Duration: ", c.execute("SELECT duration FROM dnd_spell WHERE id=?", (i,)).fetchall()
	print "Saving Throw: ", c.execute("SELECT saving_throw FROM dnd_spell WHERE id=?", (i,)).fetchall()
	print "Spell Resistance: ", c.execute("SELECT spell_resistance FROM dnd_spell WHERE id=?", (i,)).fetchall()
	print '\n'
	print c.execute("SELECT description FROM dnd_spell WHERE id=?", (i,)).fetchall()


def get_characlass(i):
	print '\n'
	print c.execute("SELECT dnd_characterclass.name FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
	print '-----------------------'
	print "Rulebook: ", c.execute("SELECT dnd_rulebook.name FROM dnd_characterclassvariant JOIN dnd_rulebook ON dnd_characterclassvariant.rulebook_id = dnd_rulebook.id JOIN dnd_characterclass ON dnd_characterclassvariant.character_class_id = dnd_characterclass.id WHERE dnd_characterclass.id =?", (i,)).fetchall()
	print "Page ", c.execute("SELECT dnd_characterclassvariant.page FROM dnd_characterclassvariant JOIN dnd_characterclass ON dnd_characterclassvariant.character_class_id = dnd_characterclass.id WHERE dnd_characterclass.id =?", (i,)).fetchall()
	print '\n'
	#print "Adventures: "
	#print "Characteristics: "
	print "Alignment: ", c.execute("SELECT dnd_characterclassvariant.alignment FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
	#print "Religion: "
	#print "Background: "
	#print "Races: "
	#print "Other Classes: "
	#print "Role: "
	print "Hit Die: ", c.execute("SELECT dnd_characterclassvariant.hit_die FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
	print "Skill Points: ", c.execute("SELECT dnd_characterclassvariant.skill_points FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
	print "Class Skills"
	print '\n'
	print "Advancement: \n", c.execute("SELECT dnd_characterclassvariant.advancement_html FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
	print '\n'
	print "Class Features: \n", c.execute("SELECT dnd_characterclassvariant.class_features FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
	print '\n'
	print "Starting Gold: ", c.execute("SELECT dnd_characterclassvariant.starting_gold FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()

def get_feat(i):
	print '\n'
	print c.execute("SELECT name FROM dnd_feat WHERE id=?", (i,)).fetchall()
	print '-----------------------'
	print '\n'
	print "Feat Category: "
	print c.execute("SELECT dnd_featcategory.name FROM dnd_feat_feat_categories JOIN dnd_feat ON dnd_feat_feat_categories.feat_id = dnd_feat.id JOIN dnd_featcategory ON dnd_feat_feat_categories.featcategory_id = dnd_featcategory.id WHERE dnd_feat.id =?", (i,)).fetchall()
	print '\n'
	print "Rulebook: ", c.execute("SELECT dnd_rulebook.name FROM dnd_feat JOIN dnd_rulebook ON dnd_feat.rulebook_id = dnd_rulebook.id WHERE dnd_feat.id =?", (i,)).fetchall()
	print '\n'
	print 'Benefit:'
	print c.execute("SELECT benefit FROM dnd_feat WHERE id=?", (i,)).fetchall()
	print '\n'
	print 'Normal:'
	print c.execute("SELECT normal FROM dnd_feat WHERE id=?", (i,)).fetchall()
	print '\n'
	print 'Special:'
	print c.execute("SELECT special FROM dnd_feat WHERE id=?", (i,)).fetchall()
	print '\n'
	print 'Description:'
	print c.execute("SELECT description FROM dnd_feat WHERE id=?", (i,)).fetchall()
	print '\n'
	print 'Requirements: '
	print '\n'
	print 'Required Feats:'
	print c.execute("SELECT dnd_feat.name, dnd_featrequiresfeat.additional_text FROM dnd_featrequiresfeat JOIN dnd_feat ON dnd_featrequiresfeat.required_feat_id = dnd_feat.id WHERE dnd_featrequiresfeat.source_feat_id =?", (i,)).fetchall()
	print '\n'
	print 'Required Skills:'
	print c.execute("SELECT dnd_skill.name, dnd_featrequiresskill.min_rank FROM dnd_featrequiresskill JOIN dnd_skill ON dnd_featrequiresskill.skill_id = dnd_skill.id JOIN dnd_feat ON dnd_featrequiresskill.feat_id = dnd_feat.id WHERE dnd_featrequiresskill.feat_id =?", (i,)).fetchall()
	print '\n'
	print 'Special Requirements:'
	print c.execute("SELECT dnd_specialfeatprerequisite.name, dnd_featspecialfeatprerequisite.value_1, dnd_featspecialfeatprerequisite.value_2 FROM dnd_featspecialfeatprerequisite JOIN dnd_feat ON dnd_featspecialfeatprerequisite.feat_id = dnd_feat.id JOIN dnd_specialfeatprerequisite ON dnd_featspecialfeatprerequisite.special_feat_prerequisite_id = dnd_specialfeatprerequisite.id WHERE dnd_featspecialfeatprerequisite.feat_id =?", (i,)).fetchall()

def get_skill(i):
	print '\n'
	print c.execute("SELECT name FROM dnd_skill WHERE id=?", (i,)).fetchall()
	print '-----------------------'
	print '\n'
	print "Rulebook: ", c.execute("SELECT dnd_rulebook.name, dnd_skillvariant.page FROM dnd_skillvariant JOIN dnd_rulebook ON dnd_skillvariant.rulebook_id = dnd_rulebook.id WHERE dnd_skillvariant.skill_id =?", (i,)).fetchall()
	print '\n'
	print "Key Ability:"
	print c.execute("SELECT base_skill FROM dnd_skill WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Trained Only:"
	if c.execute("SELECT trained_only FROM dnd_skill WHERE id=?", (i,)).fetchall()[0] == 1:
		print "Yes"
	else:
		print "No"
	print '\n'
	print "Armor Check Penalty:"
	if c.execute("SELECT armor_check_penalty FROM dnd_skill WHERE id=?", (i,)).fetchall()[0] == 1:
		print "Yes"
	else:
		print "No"
	print '\n'
	print "Description:"
	print c.execute("SELECT dnd_skillvariant.description FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
	print '\n'
	print "Check:"
	print c.execute("SELECT dnd_skillvariant.check_html FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
	print '\n'
	print "Action:"
	print c.execute("SELECT dnd_skillvariant.action FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
	print '\n'
	print "Try again:"
	print c.execute("SELECT dnd_skillvariant.try_again FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
	print '\n'
	print "Special:"
	print c.execute("SELECT dnd_skillvariant.special FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
	print '\n'
	print "Synergy:"
	print c.execute("SELECT dnd_skillvariant.synergy FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
	print '\n'
	print "Restriction:"
	print c.execute("SELECT dnd_skillvariant.restriction FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
	print '\n'
	print "Untrained:"
	print c.execute("SELECT dnd_skillvariant.untrained FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
	
def get_race(i):
	print '\n'
	print c.execute("SELECT name FROM dnd_race WHERE id=?", (i,)).fetchall()
	print '-----------------------'
	print '\n'
	print c.execute("SELECT dnd_rulebook.name, dnd_race.page FROM dnd_race JOIN dnd_rulebook ON dnd_race.rulebook_id = dnd_rulebook.id WHERE dnd_race.id =?", (i,)).fetchall()
	print '\n'
	'''print "Race Type: ", f['dnd_racetype']['name'].ix[f['dnd_race']['race_type_id'].ix[i]]
	print "Base Hit Die Size: ", f['dnd_racetype']['hit_die_size'].ix[f['dnd_race']['race_type_id'].ix[i]]
	print "Base Attack Type: ", f['dnd_racetype']['base_attack_type'].ix[f['dnd_race']['race_type_id'].ix[i]]
	print "Base Fort Save: ", f['dnd_racetype']['base_fort_save_type'].ix[f['dnd_race']['race_type_id'].ix[i]]
	print "Base Reflex Save: ", f['dnd_racetype']['base_reflex_save_type'].ix[f['dnd_race']['race_type_id'].ix[i]]
	print "Base Will Save: ", f['dnd_racetype']['base_will_save_type'].ix[f['dnd_race']['race_type_id'].ix[i]]'''
	print '\n'
	#"Personality"
	#"Physical Description"
	#"Relations"
	#"Alignment"
	#"Lands"
	#"Religion"
	#"Language"
	#"Names"
	#"Adventurers"
	print "Ability Adjustment:"
	print '\n'
	print "STR ", c.execute("SELECT str FROM dnd_race WHERE id=?", (i,)).fetchall()
	print "DEX ", c.execute("SELECT dex FROM dnd_race WHERE id=?", (i,)).fetchall()
	print "CON ", c.execute("SELECT con FROM dnd_race WHERE id=?", (i,)).fetchall()
	print "INT ", c.execute("SELECT int FROM dnd_race WHERE id=?", (i,)).fetchall()
	print "WIS ", c.execute("SELECT wis FROM dnd_race WHERE id=?", (i,)).fetchall()
	print "CHA ", c.execute("SELECT cha FROM dnd_race WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Level Adjustment", c.execute("SELECT level_adjustment FROM dnd_race WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Size:", c.execute("SELECT dnd_racesize.name FROM dnd_race JOIN dnd_racesize ON dnd_race.size_id = dnd_racesize.id WHERE dnd_race.id =?", (i,)).fetchall()
	print "Space: ", c.execute("SELECT space FROM dnd_race WHERE id=?", (i,)).fetchall()
	print "Reach: ", c.execute("SELECT reach FROM dnd_race WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Description:"
	print c.execute("SELECT description FROM dnd_race WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Racial Traits:"
	print c.execute("SELECT racial_traits FROM dnd_race WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Combat:"
	print c.execute("SELECT combat FROM dnd_race WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Natural Armor:"
	print c.execute("SELECT natural_armor FROM dnd_race WHERE id=?", (i,)).fetchall()
	print '\n'	
	print "Hit Dice Count"
	print c.execute("SELECT racial_hit_dice_count FROM dnd_race WHERE id=?", (i,)).fetchall()

def get_monster(i):
	print '\n'
	print c.execute("SELECT name FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '-----------------------'
	print '\n'
	print c.execute("SELECT dnd_rulebook.name, dnd_monster.page FROM dnd_monster JOIN dnd_rulebook ON dnd_monster.rulebook_id = dnd_rulebook.id WHERE dnd_monster.id =?", (i,)).fetchall()
	print c.execute("SELECT dnd_monstertype.name FROM dnd_monster JOIN dnd_monstertype ON dnd_monster.type_id = dnd_monstertype.id WHERE dnd_monster.id =?", (i,)).fetchall()
	print '\n'	
	print '\n'
	print "Hit Dice:", c.execute("SELECT hit_dice FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "Initiative:", c.execute("SELECT initiative FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "Speed:", c.execute("SELECT dnd_monsterspeed.speed FROM dnd_monster JOIN dnd_monsterspeed ON dnd_monster.type_id = dnd_monsterspeed.id WHERE dnd_monster.id =?", (i,)).fetchall()
	print "Armor Class:", c.execute("SELECT armor_class FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "Touch Armor Class:", c.execute("SELECT touch_armor_class FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "Flat-footed Armor Class:", c.execute("SELECT flat_footed_armor_class FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Base Attack:", c.execute("SELECT base_attack FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "Grapple:", c.execute("SELECT grapple FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "Attack:", c.execute("SELECT attack FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "Full Attack:", c.execute("SELECT full_attack FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "Special Attacks:", c.execute("SELECT special_attacks FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'	
	print "Size:", c.execute("SELECT dnd_racesize.name FROM dnd_monster JOIN dnd_racesize ON dnd_monster.size_id = dnd_racesize.id WHERE dnd_monster.id =?", (i,)).fetchall()
	print "Space: ", c.execute("SELECT space FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "Reach: ", c.execute("SELECT reach FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Special Qualities:", c.execute("SELECT special_qualities FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'	
	print "Fortitude Save:", c.execute("SELECT fort_save, fort_save_extra FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "Reflex Save:", c.execute("SELECT reflex_save, reflex_save_extra FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "Will Save:", c.execute("SELECT will_save, will_save_extra FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Ability Scores:"
	print '\n'
	print "STR ", c.execute("SELECT str FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "DEX ", c.execute("SELECT dex FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "CON ", c.execute("SELECT con FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "INT ", c.execute("SELECT int FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "WIS ", c.execute("SELECT wis FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print "CHA ", c.execute("SELECT cha FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Skills:", c.execute("SELECT dnd_skill.name FROM dnd_monsterhasskill JOIN dnd_skill ON dnd_monsterhasskill.skill_id = dnd_skill.id JOIN dnd_monster ON dnd_monsterhasskill.monster_id = dnd_monster.id WHERE dnd_monster.id =?", (i,)).fetchall()
	print '\n'
	print "Feats:", c.execute("SELECT dnd_feat.name FROM dnd_monsterhasfeat JOIN dnd_feat ON dnd_monsterhasfeat.feat_id = dnd_feat.id JOIN dnd_monster ON dnd_monsterhasfeat.monster_id = dnd_monster.id WHERE dnd_monster.id =?", (i,)).fetchall()
	print '\n'
	print "Environment:", c.execute("SELECT environment FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Organization:"
	print c.execute("SELECT organization FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Challenge Rating:", c.execute("SELECT challenge_rating FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Treasure:"
	print c.execute("SELECT treasure FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Alignment:", c.execute("SELECT alignment FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Advancement:", c.execute("SELECT advancement FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Level Adjustment:", c.execute("SELECT level_adjustment FROM dnd_race WHERE id=?", (i,)).fetchall()
	print '\n'
	print '\n'
	print "Description:"
	print c.execute("SELECT description FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Combat:"
	print c.execute("SELECT combat FROM dnd_monster WHERE id=?", (i,)).fetchall()
	print '\n'

def get_item(i):
	print '\n'
	print c.execute("SELECT name FROM dnd_item WHERE id=?", (i,)).fetchall()
	print '-----------------------'
	
	print "Rulebook: ", c.execute("SELECT dnd_rulebook.name, dnd_item.page FROM dnd_item JOIN dnd_rulebook ON dnd_item.rulebook_id = dnd_rulebook.id WHERE dnd_item.id =?", (i,)).fetchall()
	print '\n'
	print "Type: ", c.execute("SELECT type FROM dnd_item WHERE id=?", (i,)).fetchall()
	print "Price: ", c.execute("SELECT price_gp FROM dnd_item WHERE id=?", (i,)).fetchall()
	print "Item Level: ", c.execute("SELECT item_level FROM dnd_item WHERE id=?", (i,)).fetchall()
	print "Properties: ", c.execute("SELECT dnd_itemproperty.name FROM dnd_item JOIN dnd_itemproperty ON dnd_item.property_id = dnd_itemproperty.id WHERE dnd_item.id =?", (i,)).fetchall()
	print "Body Slot: ", c.execute("SELECT dnd_itemslot.name FROM dnd_item JOIN dnd_itemslot ON dnd_item.body_slot_id = dnd_itemslot.id WHERE dnd_item.id =?", (i,)).fetchall()
	print "Caster Level: ", c.execute("SELECT caster_level FROM dnd_item WHERE id=?", (i,)).fetchall()
	print "Aura: ", c.execute("SELECT dnd_itemauratype.name, dnd_item.aura_dc FROM dnd_item JOIN dnd_itemauratype ON dnd_item.aura_id = dnd_itemauratype.id WHERE dnd_item.id =?", (i,)).fetchall()
	print "Aura School: ", c.execute("SELECT dnd_spellschool.name FROM dnd_item_aura_schools JOIN dnd_item ON dnd_item_aura_schools.item_id = dnd_item.id JOIN dnd_spellschool ON dnd_item_aura_schools.spellschool_id = dnd_spellschool.id WHERE dnd_item.id =?", (i,)).fetchall()
	print "Activation: ", c.execute("SELECT dnd_itemactivationtype.name FROM dnd_item JOIN dnd_itemactivationtype ON dnd_item.activation_id = dnd_itemactivationtype.id WHERE dnd_item.id =?", (i,)).fetchall()
	print "Weight: ", c.execute("SELECT weight FROM dnd_item WHERE id=?", (i,)).fetchall()
	print "Visual Description: ", c.execute("SELECT visual_description FROM dnd_item WHERE id=?", (i,)).fetchall()
	print "Description: ", c.execute("SELECT description FROM dnd_item WHERE id=?", (i,)).fetchall()
#	print "Relic Power: ",
#	print "Lore: ",
	print "Prerequisites: "
	print '\n'
	print "Required Feats: ", c.execute("SELECT dnd_feat.name FROM dnd_item_required_feats JOIN dnd_item ON dnd_item_required_feats.item_id = dnd_item.id JOIN dnd_feat ON dnd_item_required_feats.feat_id = dnd_feat.id WHERE dnd_item.id =?", (i,)).fetchall()	
	print "Required Spells: ", c.execute("SELECT dnd_spell.name FROM dnd_item_required_spells JOIN dnd_item ON dnd_item_required_spells.item_id = dnd_item.id JOIN dnd_spell ON dnd_item_required_spells.spell_id = dnd_spell.id WHERE dnd_item.id =?", (i,)).fetchall()
	print "Synergy Prerequisites: ",
#	print "Extra Prerequisites: ", c.execute("SELECT required_extra FROM dnd_item WHERE id=?", (i,)).fetchall()
	print '\n'
	print "Cost to Create: ", c.execute("SELECT cost_to_create FROM dnd_item WHERE id=?", (i,)).fetchall()
	print '\n'

def get_deity(i):
	"Name"
	"Domain"
	"Alignment"
	"Description"

#PROTOTYPE SORTING ALGORITHM; lists spells for a given class.

def spell_by_class(cl):
	sbcl = c.execute("SELECT dnd_spell.id, dnd_spell.name, dnd_characterclass.name, dnd_spellclasslevel.level FROM dnd_spellclasslevel LEFT JOIN dnd_spell ON dnd_spellclasslevel.spell_id = dnd_spell.id LEFT JOIN dnd_characterclass ON dnd_spellclasslevel.character_class_id = dnd_characterclass.id WHERE dnd_characterclass.id =? ORDER BY dnd_spellclasslevel.level", (cl,)).fetchall()
	for i in sbcl:
		print i



filter_dict = \
{
	'dnd_spell' :
	{
		'rulebook_id' : 6,
		'class' : 2,
		'domain' : None,
		'classlevel' : 5,
		'domlevel' : None,
		'effect' : None,
		'school_id' : None,
		'sub_school_id' : None,
		'casting_time' : None,
		'range' : None,
		'components' : None,
		'saving_throw' : None,
		'descriptor' : None,
		'spell_resistance' : None,
		'description' : None
	},
	'dnd_characterclass' :
	{
		'rulebook_id': 6,
		'alignment': None,
		'hit_die': None,
		'skill_points': None
	},
	'dnd_feat' :
	{
		'rulebook_id': 6,
		'feat_category': None
	},
	'dnd_skill' :
	{
		'rulebook_id': 6,
		'key_ability': None
	},
	'dnd_race' : 
	{
		'rulebook_id':6,
		'str': None,
		'dex': None,
		'con': None,
		'int': None,
		'wis': None,
		'cha': None,
		'level_adj': None,
		'size': None,
		'space': None,
		'reach': None,
		'natural_armor': None,
		'hit_dice_count': None
	},
	'dnd_monster' :
	{
		'rulebook_id':6,
		'type': None,
		'challenge_rating': None,
		'hit_dice': None,
		'initiative': None,
		'speed': None,
		'armor_class': None,
		'size': None,
		'space': None,
		'reach': None,
		'str': None,
		'dex': None,
		'con': None,
		'int': None,
		'wis': None,
		'cha': None,
		'environment': None,
		'alignment': None
	},
	'dnd_item' :
	{
		'rulebook_id':6,
		'type': None,
		'price': None,
		'item_level': None,
		'properties': None,
		'body_slot': None,
		'caster_level': None,
		'aura': None,
		'aura_school': None,
		'activation': None,
		
	}
 }


sortby_dict = \
{
	'dnd_spell' :
	{
		'classlevel':
		{
			'order' : " ORDER BY dnd_spellclasslevel.character_class_id, dnd_spellclasslevel.level",
			'join' : "JOIN dnd_spellclasslevel ON dnd_spell.id = dnd_spellclasslevel.spell_id"
		},
		'domlevel':
		{
			'order' : " ORDER BY dnd_spelldomainlevel.domain_id, dnd_spelldomainlevel.level",
			'join' : "JOIN dnd_spelldomainlevel ON dnd_spell.id = dnd_spelldomainlevel.domain_id"
		},	
		'spelldescriptor':
		{
			'order' : " ORDER BY dnd_spelldescriptor.name",
			'join' : "JOIN dnd_spell_descriptors ON dnd_spell.id = dnd_spell_descriptors.spell_id JOIN dnd_spelldescriptor ON dnd_spell_descriptors.spelldescriptor_id = dnd_spelldescriptor.id"
		},
		'rulebook_id':
		{
			'order' : " ORDER BY dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_spell.rulebook_id = dnd_rulebook.id"
		},
		'name' :
		{
			'order' : " ORDER BY dnd_spell.name",
			'join' : ""
		},
		'school_id':
		{
			'order' : " ORDER BY dnd_spellschool.name",
			'join' : "JOIN dnd_spellschool ON dnd_spell.school_id = dnd_spellschool.id"
		}
	},

	'dnd_characterclass' :
	{
		'rulebook_id':
		{
			'order' : " ORDER BY dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_characterclass.rulebook_id = dnd_rulebook.id"
		},
		'name' :
		{
			'order' : " ORDER BY dnd_characterclass.name",
			'join' : ""
		},
		'alignment':
		{
			'order' : " ORDER BY dnd_characterclassvariant.alignment",
			'join' : "JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id"
		},
		'hit_die':
		{
			'order' : " ORDER BY dnd_characterclassvariant.hit_die",
			'join' : "JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id"
		},
		'skill_points':
		{
			'order' : " ORDER BY dnd_characterclassvariant.skill_points",
			'join' : "JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id"
		}
	},
	
	'dnd_feat' :
	{
		'rulebook_id':
		{
			'order' : " ORDER BY dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_feat.rulebook_id = dnd_rulebook.id"
		},
		'name' :
		{
			'order' : " ORDER BY dnd_feat.name",
			'join' : ""
		},
		'feat_category':
		{
			'order' : " ORDER BY dnd_featcategory.name",
			'join' : "JOIN dnd_feat_feat_categories ON dnd_feat.id = dnd_feat_feat_categories.feat_id JOIN dnd_featcategory ON dnd_feat_feat_categories.featcategory.id = dnd_featcategory.id"
		}
	},
	
	'dnd_skill' :
	{
		'rulebook_id':
		{
			'order' : " ORDER BY dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_skill.rulebook_id = dnd_rulebook.id"
		},
		'name' :
		{
			'order' : " ORDER BY dnd_skill.name",
			'join' : ""
		},
		'base_skill' :
		{
			'order' : " ORDER BY dnd_skill.base_skill",
			'join' : ""
		}
	},

	'dnd_race' : 
	{
		'rulebook_id':
		{
			'order' : " ORDER BY dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_race.rulebook_id = dnd_rulebook.id"
		},
		'name' :
		{
			'order' : " ORDER BY dnd_race.name",
			'join' : ""
		},
		'str' :
		{
			'order' : " ORDER BY dnd_race.str",
			'join' : ""
		},
		'dex' :
		{
			'order' : " ORDER BY dnd_race.dex",
			'join' : ""
		},
		'con' :
		{
			'order' : " ORDER BY dnd_race.con",
			'join' : ""
		},
		'int' :
		{
			'order' : " ORDER BY dnd_race.int",
			'join' : ""
		},
		'wis' :
		{
			'order' : " ORDER BY dnd_race.wis",
			'join' : ""
		},
		'cha' :
		{
			'order' : " ORDER BY dnd_race.cha",
			'join' : ""
		},
		'level_adjustment' :
		{
			'order' : " ORDER BY dnd_race.level_adjustment",
			'join' : ""
		},
		'size' :
		{
			'order' : " ORDER BY dnd_race.size",
			'join' : ""
		},
		'space' :
		{
			'order' : " ORDER BY dnd_race.space",
			'join' : ""
		},
		'reach' :
		{
			'order' : " ORDER BY dnd_race.reach",
			'join' : ""
		},
		'natural_armor' :
		{
			'order' : " ORDER BY dnd_race.natural_armor",
			'join' : ""
		},
		'racial_hit_dice_count' :
		{
			'order' : " ORDER BY dnd_race.racial_hit_dice_count",
			'join' : ""
		}
	},
	
	'dnd_monster' :
	{
		'rulebook_id':
		{
			'order' : " ORDER BY dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_monster.rulebook_id = dnd_rulebook.id"
		},
		'name' :
		{
			'order' : " ORDER BY dnd_monster.name",
			'join' : ""
		},
		'challenge_rating' :
		{
			'order' : " ORDER BY dnd_monster.challenge_rating",
			'join' : ""
		},
		'size' :
		{
			'order' : " ORDER BY dnd_racesize.order",
			'join' : "JOIN dnd_racesize on dnd_monster.size_id = dnd_racesize.id"
		},
		'type' :
		{
			'order' : " ORDER BY dnd_monstertype.name",
			'join' : "JOIN dnd_monstertype on dnd_monster.type_id = dnd_monstertype.id"
		},
		'hit_dice' :
		{
			'order' : " ORDER BY dnd_monster.hit_dice",
			'join' : ""
		},
		'armor_class' :
		{
			'order' : " ORDER BY dnd_monster.armor_class",
			'join' : ""
		},
		'base_attack' :
		{
			'order' : " ORDER BY dnd_monster.base_attack",
			'join' : ""
		},
		'space' :
		{
			'order' : " ORDER BY dnd_monster.space",
			'join' : ""
		},
		'reach' :
		{
			'order' : " ORDER BY dnd_monster.reach",
			'join' : ""
		},
		'fort_save' :
		{
			'order' : " ORDER BY dnd_monster.fort_save",
			'join' : ""
		},
		'reflex_save' :
		{
			'order' : " ORDER BY dnd_monster.reflex_save",
			'join' : ""
		},
		'will_save' :
		{
			'order' : " ORDER BY dnd_monster.reflex_save",
			'join' : ""
		},
		'str' :
		{
			'order' : " ORDER BY dnd_monster.str",
			'join' : ""
		},
		'dex' :
		{
			'order' : " ORDER BY dnd_monster.dex",
			'join' : ""
		},
		'con' :
		{
			'order' : " ORDER BY dnd_monster.con",
			'join' : ""
		},
		'int' :
		{
			'order' : " ORDER BY dnd_monster.int",
			'join' : ""
		},
		'wis' :
		{
			'order' : " ORDER BY dnd_monster.wis",
			'join' : ""
		},
		'cha' :
		{
			'order' : " ORDER BY dnd_monster.cha",
			'join' : ""
		},
		'environment' :
		{
			'order' : " ORDER BY dnd_monster.environment",
			'join' : ""
		},
		'organization' :
		{
			'order' : " ORDER BY dnd_monster.organization",
			'join' : ""
		},
		'level_adjustment' :
		{
			'order' : " ORDER BY dnd_monster.level_adjustment",
			'join' : ""
		}
	},

	'dnd_item' :
	{
		'rulebook_id':
		{
			'order' : " ORDER BY dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_item.rulebook_id = dnd_rulebook.id"
		},		
		'name' :
		{
			'order' : " ORDER BY dnd_item.name",
			'join' : ""
		},		
		'type' :
		{
			'order' : " ORDER BY dnd_item.type",
			'join' : ""
		},		
		'price' :
		{
			'order' : " ORDER BY dnd_item.price_gp",
			'join' : ""
		},		
		'item_level' :
		{
			'order' : " ORDER BY dnd_item.item_level",
			'join' : ""
		},
		'property' :
		{
			'order' : " ORDER BY dnd_itemproperty.name",
			'join' : "JOIN dnd_itemproperty ON dnd_item.property_id = dnd_itemproperty.id"
		},
		'body_slot' :
		{
			'order' : " ORDER BY dnd_itemslot.name",
			'join' : "JOIN dnd_itemslot ON dnd_item.body_slot_id = dnd_itemslot.id"
		},
		'caster_level' :
		{
			'order' : " ORDER BY dnd_item.caster_level",
			'join' : ""
		},
		'aura' :
		{
			'order' : " ORDER BY dnd_itemauratype.name",
			'join' : "JOIN dnd_itemauratype ON dnd_item.aura_id = dnd_itemauratype.id"
		},
		'aura_school' :
		{
			'order' : " ORDER BY dnd_spellschool.name",
			'join' : "JOIN dnd_item_aura_schools ON dnd_item.id = dnd_item_aura_schools.item_id JOIN dnd_spellschool ON dnd_item_aura_schools.spellschool_id = dnd_spellschool.id"
		},
		'activation' :
		{
			'order' : " ORDER BY dnd_itemactivationtype.name",
			'join' : "JOIN dnd_itemactivationtype ON dnd_item.activation_id = dnd_itemactivationtype.id"
		},		
	}
 }
		
runtime_dict = {}

	
class dnd_query(object):
	
	def __init__(self, q_table, filt_bool, search_bool, sortby_bool, call_term, sort_key):
		self.q_table = q_table
		self.filt_bool = filt_bool
		self.search_bool = search_bool
		self.sortby_bool = sortby_bool
		self.call_term = call_term
		self.sort_key = sort_key
		
#		self.filter_dict = filter_dict
#		self.sortby_dict = sortby_dict

		self.default_str = "SELECT dnd_spell.id, dnd_spell.name FROM dnd_spell "
		self.join_str = []
		self.where_str = {}
		self.sortby_str = []
		self.str_li = []
		self.q_str = ""

	def init_filter(self):
		pass

	def init_sortby(self):
		pass
		
	def make_sp_filter_inner(self, **kwargs):
		
		if kwargs['rulebook_id'] == None:
			pass
		else:
			self.where_str.update({'dnd_spell.rulebook_id': ["=", "", str(kwargs['rulebook_id']), ""]})
		# WHERE =
		if kwargs['class'] == None:
			pass
		else:
			self.where_str.update({'dnd_spellclasslevel.character_class_id': ["=", "", str(kwargs['class']), ""]})
			self.join_str.append("JOIN dnd_spellclasslevel ON dnd_spell.id = dnd_spellclasslevel.spell_id")

		if kwargs['domain'] == None:
			pass
		else:
			self.where_str.update({'dnd_spelldomainlevel.domain_id': ["=", "", str(kwargs['domain']), ""]})
			self.join_str.append("JOIN dnd_spelldomainlevel ON dnd_spell.id = dnd_spelldomainlevel.spell_id")

		if kwargs['classlevel'] == None:
			pass
		else:
			self.where_str.update({'dnd_spellclasslevel.level': ["=", "", str(kwargs['classlevel']), ""]})
			self.join_str.append("JOIN dnd_spellclasslevel ON dnd_spell.id = dnd_spellclasslevel.spell_id")

		if kwargs['domlevel'] == None:
			pass
		else:
			self.where_str.update({'dnd_spelldomainlevel.level': ["=", "", str(kwargs['domlevel']), ""]})	
			self.join_str.append("JOIN dnd_spelldomainlevel ON dnd_spell.id = dnd_spelldomainlevel.spell_id")
		
		if kwargs['effect'] == None:
			pass
		else:
			self.where_str.update({'dnd_spell.effect': [" LIKE ", "'%", str(kwargs['effect']), "%'"]})
		
		if kwargs['school_id'] == None:
			pass
		else:
			self.where_str.update({'dnd_spell.school_id': ["=", "", str(kwargs['school_id']), ""]})
	
		if kwargs['sub_school_id'] == None:
			pass
		else:
			self.where_str.update({'dnd_spell.sub_school_id': ["=", "", str(kwargs['sub_school_id']), ""]})
	
		if kwargs['casting_time'] == None:
			pass
		else:
			self.where_str.update({'dnd_spell.casting_time': [" LIKE ", "'%", str(kwargs['casting_time']), "%'"]})
	
		if kwargs['range'] == None:
			pass
		else:
			self.where_str.update({'dnd_spell.range': [" LIKE ", "'%", str(kwargs['range']), "%'"]})

		
	#	if kwargs['components'] == None:
	#		pass
	#	else:
	#		where_str.update({'dnd_spell.verbal_component': str(kwargs['components'])})
	
		if kwargs['saving_throw'] == None:
			pass
		else:
			self.where_str.update({'dnd_spell.saving_throw': str(kwargs['saving_throw'])})

			
	#	if kwargs['descriptor'] == None:
	#		pass
	#	else:
	#		where_str.update({'dnd_spell_descriptors.spelldescriptor.id': str(kwargs['descriptor'])})
	#		join_str.append("JOIN dnd_spell_descriptors ON dnd_spell.id = dnd_spell_descriptors.spell_id")
	
		if kwargs['spell_resistance'] == None:
			pass
		else:
			self.where_str.update({'dnd_spell.spell_resistance': str(kwargs['spell_resistance'])})

		
		if kwargs['description'] == None:
			pass
		else:
			self.where_str.update({'dnd_spell.description': str(kwargs['description'])})
		print 'sp_filt', self.join_str
		print '\n'
		print 'sp_filt', self.where_str
		print '\n'
		print '\n'
		
	def search_tables(self, term):
		self.where_str.update({'dnd_spell.name': [" LIKE ", "'%", term, "%'"]})
		print 'search', self.where_str
	
	def sortby(self):
		self.join_str.append(sortby_dict[self.q_table][self.sort_key]['join'])
		self.sortby_str.append(sortby_dict[self.q_table][self.sort_key]['order'])
		print 'sortby', self.join_str
		print 'sortby', self.sortby_str

	def submit_query(self):
	
		if self.filt_bool == True:
			self.make_sp_filter_inner(**filter_dict[self.q_table])
		else:
			pass
		if self.search_bool == True:
			self.search_tables(self.call_term)
		else:
			pass
		if self.sortby_bool == True:
			self.sortby()
		else:
			pass
		
		self.join_str = list(set(self.join_str))
		self.sortby_str = list(set(self.sortby_str))
#		print join_str
		
		for k, v in self.where_str.iteritems():
			self.str_li.append(k + str(v[0]) + str(v[1]) + str(v[2]) + str(v[3]))
#		
		self.str_li = list(set(self.str_li))
		self.where_query = ' AND '.join(self.str_li)
		self.join_query = ' '.join(self.join_str)
		self.sortby_query = ' '.join(self.sortby_str)
	
		print self.where_query
		print self.join_query
		print self.sortby_query
		
		if len(self.where_query) > 0:
			self.q_str = self.default_str + self.join_query + " WHERE " + self.where_query + self.sortby_query
			print self.q_str
			filt_result = c.execute(self.q_str).fetchall()
			for i in filt_result:
				print i
			self.default_str = "SELECT dnd_spell.id, dnd_spell.name FROM dnd_spell "
			self.join_str = []
			self.where_str = {}
			self.sortby_str = []
			self.str_li = []
			self.q_str = ""
			self.where_query = ""
			self.join_query = ""
			self.sortby_query = ""		
		else:
			self.q_str = self.default_str + self.join_query + self.sortby_query
			print self.q_str
			filt_result = c.execute(self.q_str).fetchall()
			for i in filt_result:
				print i		
			self.default_str = "SELECT dnd_spell.id, dnd_spell.name FROM dnd_spell "
			self.join_str = []
			self.where_str = {}
			self.sortby_str = []
			self.str_li = []
			self.q_str = ""
			self.where_query = ""
			self.join_query = ""
			self.sortby_query = ""		