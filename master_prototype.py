#Initialize

import numpy as np
import pandas as pd
import sqlite3
import ast
import html5lib

#Connect to database in current directory (database must be downloaded elsewhere and placed in current directory)

conn = sqlite3.connect('dnd.sqlite')
c = conn.cursor()
conn.text_factory = str

''' c.execute("SELECT name FROM sqlite_master WHERE type='table';")'''

#Copy database tables, convert to pandas dataframes, append dataframes to dict "f"
f = {}

table_container = ['dnd_characterclass', 'dnd_characterclassvariant', 'dnd_characterclassvariant_class_skills', 'dnd_characterclassvariantrequiresfeat', 'dnd_characterclassvariantrequiresrace', 'dnd_characterclassvariantrequiresskill', 'dnd_deity', 'dnd_dndedition', 'dnd_domain', 'dnd_domainvariant', 'dnd_domainvariant_deities', 'dnd_feat', 'dnd_feat_feat_categories', 'dnd_featcategory', 'dnd_featrequiresfeat', 'dnd_featrequiresskill', 'dnd_featspecialfeatprerequisite', 'dnd_item', 'dnd_item_aura_schools', 'dnd_item_required_feats', 'dnd_item_required_spells', 'dnd_itemactivationtype', 'dnd_itemauratype', 'dnd_itemproperty', 'dnd_itemslot', 'dnd_language', 'dnd_monster', 'dnd_monster_subtypes', 'dnd_monsterhasfeat', 'dnd_monsterhasskill', 'dnd_monsterspeed', 'dnd_monstersubtype', 'dnd_monstertype', 'dnd_newsentry', 'dnd_race', 'dnd_race_automatic_languages', 'dnd_race_bonus_languages', 'dnd_racefavoredcharacterclass', 'dnd_racesize', 'dnd_racespeed', 'dnd_racespeedtype', 'dnd_racetype', 'dnd_rule', 'dnd_rulebook', 'dnd_skill', 'dnd_skillvariant', 'dnd_specialfeatprerequisite', 'dnd_spell', 'dnd_spell_descriptors', 'dnd_spellclasslevel', 'dnd_spelldescriptor', 'dnd_spelldomainlevel', 'dnd_spellschool', 'dnd_spellsubschool', 'dnd_staticpage', 'dnd_textfeatprerequisite', 'dnd_rules_conditions']

for index, item in enumerate(table_container):
	f.update({table_container[index]: pd.DataFrame(c.execute("SELECT * from %s" % (item)).fetchall())})

for key, frame in f.items():
	query = c.execute("SELECT * from %s" % (key))
	names = list(map(lambda x: x[0], c.description))
	f[key].columns = names

conn.close()


for key, value in f.iteritems():
	f[key] = f[key].set_index('id')

#temp; replace 'dnd_spell' with modified csv (optimizes page call speed). csv must be placed in current directory.
spellimport = pd.read_csv('spell_w_class_and_dom.csv')	
spellimport = spellimport.set_index('id')
f['dnd_spell'] = spellimport
#

'''

f['dnd_spell']['classlv_dict'] = 0


for i in f['dnd_spell'].index:
	dict = {}
	for j, s in f['dnd_spellclasslevel'].iterrows():
		if f['dnd_spellclasslevel']['spell_id'].ix[j] == i:
			dict.update({f['dnd_spellclasslevel']['character_class_id'].ix[j]: f['dnd_spellclasslevel']['level'].ix[j]})
			f['dnd_spell']['classlv_dict'].ix[i] = dict

f['dnd_spell']['domlv_dict'] = 0

for i in f['dnd_spell'].index:
	ddict = {}
	for j, s in f['dnd_spelldomainlevel'].iterrows():
		if f['dnd_spelldomainlevel']['spell_id'].ix[j] == i:
			ddict.update({f['dnd_spelldomainlevel']['domain_id'].ix[j]: f['dnd_spelldomainlevel']['level'].ix[j]})
			f['dnd_spell']['domlv_dict'].ix[i] = ddict

'''

#Page call functions
		
def get_spell(i):
	print '\n'
	print f['dnd_spell']['name'].ix[i]
	print '-----------------------'
	print "Rulebook: ", f['dnd_rulebook']['name'].ix[f['dnd_spell']['rulebook_id'].ix[i]]
	print f['dnd_spellschool']['name'].ix[f['dnd_spell']['school_id'].ix[i]]
	print '\n'
	'''if f['dnd_spell']['sub_school_id'].ix[i] == 'NaN':
		pass
	else:
		print f['dnd_spellsubschool']['name'].ix[f['dnd_spell']['sub_school_id'].ix[i]]'''
	if f['dnd_spell']['classlv_dict'].ix[i] == 0:
		pass
	elif f['dnd_spell']['classlv_dict'].ix[i] == '0':
		pass
	else:
		classdict = ast.literal_eval(f['dnd_spell']['classlv_dict'].ix[i])
		for key in classdict.iterkeys():
			print f['dnd_characterclass']['name'].ix[key], classdict[key]
	if f['dnd_spell']['domlv_dict'].ix[i] == 0:
		pass
	elif f['dnd_spell']['domlv_dict'].ix[i] == '0':
		pass
	else:
		domdict = ast.literal_eval(f['dnd_spell']['domlv_dict'].ix[i])
		for dkey in domdict.iterkeys():
			print f['dnd_characterclass']['name'].ix[dkey], domdict[dkey]
	print '\n'		
	print "Casting Time: ", f['dnd_spell']['casting_time'].ix[i]
	print "Range: ", f['dnd_spell']['range'].ix[i]
	print "Target: ", f['dnd_spell']['target'].ix[i]
	print "Effect: ", f['dnd_spell']['effect'].ix[i]
	print "Area: ", f['dnd_spell']['area'].ix[i]
	print "Duration: ", f['dnd_spell']['duration'].ix[i]
	print "Saving Throw: ", f['dnd_spell']['saving_throw'].ix[i]
	print "Spell Resistance: ", f['dnd_spell']['spell_resistance'].ix[i]
	print '\n'
	print f['dnd_spell']['description'].ix[i]

#Warning: inconsistent indexing; should be redone.

def get_characlass(i):
	print '\n'
	print f['dnd_characterclass']['name'].ix[f['dnd_characterclassvariant']['character_class_id'].ix[i]]
	print '-----------------------'
	print "Rulebook: ", f['dnd_rulebook']['name'].ix[f['dnd_characterclassvariant']['rulebook_id'].ix[i]]
	print "Page ", f['dnd_characterclassvariant']['page'].ix[i]
	print '\n'
	#print "Adventures: "
	#print "Characteristics: "
	print "Alignment: ", f['dnd_characterclassvariant']['alignment'].ix[i]
	#print "Religion: "
	#print "Background: "
	#print "Races: "
	#print "Other Classes: "
	#print "Role: "
	print "Hit Die:  d", f['dnd_characterclassvariant']['hit_die'].ix[i]
	print "Skill Points: ", f['dnd_characterclassvariant']['skill_points'].ix[i]
	print "Class Skills"
	print '\n'
	print "Advancement: \n", pd.read_html(f['dnd_characterclassvariant']['advancement_html'].ix[1])
	print '\n'
	print "Class Features: \n", f['dnd_characterclassvariant']['class_features'].ix[i]
	print '\n'
	print "Starting Gold: ", f['dnd_characterclassvariant']['starting_gold'].ix[i]

def get_feat(i):
	print '\n'
	print f['dnd_feat']['name'].ix[i]
	print '-----------------------'
	print '\n'
	print "Feat Category: "
	cat_ft = f['dnd_featcategory']['name'].ix[f['dnd_feat_feat_categories']['featcategory_id'].ix[f['dnd_feat_feat_categories'][f['dnd_feat_feat_categories']['feat_id'] == i].index]].get_values()
	for j in cat_ft:
		print j
	print '\n'
	print "Rulebook: ", f['dnd_rulebook']['name'].ix[f['dnd_feat']['rulebook_id'].ix[i]]
	print '\n'
	print 'Benefit:'
	print f['dnd_feat']['benefit'].ix[i]
	print '\n'
	print 'Normal:'
	print f['dnd_feat']['normal'].ix[i]
	print '\n'
	print 'Special:'
	print f['dnd_feat']['special'].ix[i]
	print '\n'
	print 'Description:'
	print f['dnd_feat']['description'].ix[i]
	print '\n'
	print 'Requirements: '
	print '\n'
	print 'Required Feats:'
	req_ft = f['dnd_feat']['name'].ix[f['dnd_featrequiresfeat']['required_feat_id'].ix[f['dnd_featrequiresfeat'][f['dnd_featrequiresfeat']['source_feat_id'] == i].index]].get_values()
	add_txt = f['dnd_featrequiresfeat']['additional_text'].ix[f['dnd_featrequiresfeat'][f['dnd_featrequiresfeat']['source_feat_id'] == i].index].get_values()
	for k in zip(req_ft, add_txt):
		if len(k[1]) < 1:
			print k[0]
		else:
			print k[0] + ' (' + k[1] + ')'
	print '\n'
	print 'Required Skills:'
	req_sk = f['dnd_feat']['name'].ix[f['dnd_featrequiresskill']['skill_id'].ix[f['dnd_featrequiresskill'][f['dnd_featrequiresskill']['feat_id'] == i].index]].get_values()
	req_sk_lv = f['dnd_featrequiresskill']['min_rank'].ix[f['dnd_featrequiresskill'][f['dnd_featrequiresskill']['feat_id'] == i].index].get_values()
	for m in zip(req_sk, req_sk_lv):
		print m[0], m[1]
	print '\n'
	print 'Special Requirements:'
	req_sp_nm = f['dnd_specialfeatprerequisite']['name'].ix[f['dnd_featspecialfeatprerequisite']['special_feat_prerequisite_id'].ix[f['dnd_featspecialfeatprerequisite'].ix[f['dnd_featspecialfeatprerequisite']['feat_id'] == i].index]].get_values()
	req_sp_val_1 = f['dnd_featspecialfeatprerequisite']['value_1'].ix[f['dnd_featspecialfeatprerequisite'].ix[f['dnd_featspecialfeatprerequisite']['feat_id'] == i].index]
	req_sp_val_2 = f['dnd_featspecialfeatprerequisite']['value_2'].ix[f['dnd_featspecialfeatprerequisite'].ix[f['dnd_featspecialfeatprerequisite']['feat_id'] == i].index]
	for n in zip(req_sp_nm, req_sp_val_1, req_sp_val_2):
		print n[0], n[1], n[2]
		

def get_skill(i):
	var_idx = f['dnd_skillvariant'][f['dnd_skillvariant']['skill_id'] == i].index
	print '\n'
	print f['dnd_skill']['name'].ix[i]
	print '-----------------------'
	print '\n'
	print '\n'.join(f['dnd_rulebook']['name'].ix[f['dnd_skillvariant']['rulebook_id'].ix[var_idx]].values)
	print "Page", f['dnd_skillvariant']['page'].ix[var_idx].values[0]
	print '\n'
	print "Key Ability:"
	print f['dnd_skill']['base_skill'].ix[i]
	print '\n'
	print "Trained Only:"
	if f['dnd_skill']['trained_only'].ix[i] == 1:
		print "Yes"
	else:
		print "No"
	print '\n'
	print "Armor Check Penalty:"
	if f['dnd_skill']['armor_check_penalty'].ix[i] == 1:
		print "Yes"
	else:
		print "No"
	print '\n'
	print "Description:"
	print '\n'.join(f['dnd_skillvariant']['description'].ix[var_idx].values)
	print '\n'
	print "Check:"
	print '\n'.join(f['dnd_skillvariant']['check'].ix[var_idx].values)
	print '\n'
	print "Action:"
	print '\n'.join(f['dnd_skillvariant']['action'].ix[var_idx].values)
	print '\n'
	print "Try again:"
	print '\n'.join(f['dnd_skillvariant']['try_again'].ix[var_idx].values)
	print '\n'
	print "Special:"
	print '\n'.join(f['dnd_skillvariant']['special'].ix[var_idx].values)
	print '\n'
	print "Synergy:"
	print '\n'.join(f['dnd_skillvariant']['synergy'].ix[var_idx].values)
	print '\n'
	print "Restriction:"
	print '\n'.join(f['dnd_skillvariant']['restriction'].ix[var_idx].values)
	print '\n'
	print "Untrained:"
	print '\n'.join(f['dnd_skillvariant']['untrained'].ix[var_idx].values)
	
def get_race(i):
	print '\n'
	print f['dnd_race']['name'].ix[i]
	print '-----------------------'
	print '\n'
	print f['dnd_rulebook']['name'].ix[f['dnd_race']['rulebook_id'].ix[i]]
	print "Page", f['dnd_race']['page'].ix[i]
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
	print "STR ", f['dnd_race']['str'].ix[i]
	print "DEX ", f['dnd_race']['dex'].ix[i]
	print "CON ", f['dnd_race']['con'].ix[i]
	print "INT ", f['dnd_race']['int'].ix[i]
	print "WIS ", f['dnd_race']['wis'].ix[i]
	print "CHA ", f['dnd_race']['cha'].ix[i]
	print '\n'
	print "Level Adjustment", f['dnd_race']['level_adjustment'].ix[i]
	print '\n'
	print "Size: ", f['dnd_racesize']['name'].ix[f['dnd_race']['space'].ix[i]]
	print "Space: ", f['dnd_race']['space'].ix[i]
	print "Reach: ", f['dnd_race']['reach'].ix[i]
	print '\n'
	print "Description:"
	print f['dnd_race']['description'].ix[i]
	print '\n'
	print "Racial Traits:"
	print f['dnd_race']['racial_traits'].ix[i]
	print '\n'
	print "Combat:"
	print f['dnd_race']['combat'].ix[i]
	print '\n'
	print "Natural Armor:"
	print f['dnd_race']['natural_armor'].ix[i]
	print '\n'	
	print "Hit Dice Count"
	print f['dnd_race']['racial_hit_dice_count'].ix[i]

def get_monster(i):
	pass

def get_deity(i):
	"Name"
	"Domain"
	"Alignment"
	"Description"

#PROTOTYPE SORTING ALGORITHM; lists spells for a given class.

def spell_by_class(c):
	sp_cl = []
	for i in f['dnd_spell'].index:
		cell = ast.literal_eval(f['dnd_spell']['classlv_dict'].ix[i])
		if cell != 0:
			cell = dict(cell)
			for key in cell.iterkeys():
				if key == c:
					sp_cl.append(i)
			else:
				continue
	return f['dnd_spell']['name'].ix[sp_cl]

#PROTOTYPE; MAY BE BUGGY; Displays all spells and class levels for a particular class.

def spell_by_class_lv(c):
	sp_cv = []
	sp_lv = []
	for i in f['dnd_spell'].index:
		cell = ast.literal_eval(f['dnd_spell']['classlv_dict'].ix[i])
		if cell != 0:
			cell = dict(cell)
			for key, value in cell.iteritems():
				if key == c:
					sp_cv.append(i)
					sp_lv.append(value)
			else:
				continue
	temp_name = f['dnd_spell']['name'].ix[sp_cv]
	temp_lv = pd.Series(sp_lv, index=sp_cv)
	output =  pd.concat([temp_name, temp_lv], axis=1)
	output.columns = ('Name', 'Class Level')
	print f['dnd_characterclass']['name'].ix[c], "Spells"
	return output.sort(columns='Class Level', ascending=True)

'''def sp_filter_bool(tf):
	if tf == True:
		return True
	else:
		return False
	filter_list = []
	if filter_cla = True
		fi_li.append(output['class'] == cla)

#df[(df.A == 1) & (df.D == 6)]'''