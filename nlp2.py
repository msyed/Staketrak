# -*- coding: utf-8 -*-
import nltk
def extract_entities(text):
	for sent in nltk.sent_tokenize(text):
		for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
			#if hasattr(chunk, 'node'):
			try:
				print chunk, 'testing'.join(c[0] for c in chunk.leaves())
			except AttributeError:
				continue
x = "PARIS — The Paris area reeled Friday night from a shooting rampage, explosions and mass hostage-taking that President François Hollande called an unprecedented terrorist attack on France. He closed the borders and mobilized the military in a national emergency.French television and news services quoted the police as saying around 100 people had been killed at a concert venue where hostages had been taken, and dozens more killed in apparently coordinated attacks outside the country’s main sports stadium and at least five other popular locations in the city.Witnesses on French television said the scene at the concert was a massacre. Ambulances were seen racing back and forth in the area into the early hours of Saturday morning.The casualties eclipsed the deaths and mayhem that roiled Paris in the Charlie Hebdo massacre and related assaults around the French capital by Islamic militant extremists less than a year ago.Continue reading the main story RELATED COVERAGE Live Coverage: Updates on the Paris Attacks An explosion near the sports stadium, which French news services said may have been a suicide bombing, came as Germany and France were playing a soccer match, forcing a hasty evacuation of Mr. Hollande. As the scope of the assaults quickly became clear, he convened an emergency cabinet meeting and announced that France was closing its borders. Barack Obama"

extract_entities(x)