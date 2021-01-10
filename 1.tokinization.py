# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 13:40:05 2020

@author: I340968
"""

import nltk
#nltk.download()
para="""I have three visions for India.In 3000 years of our history, 
        people from all over the world have come and invaded us, captured our lands and conquered our minds. 
        Yet, we have not conquered anyone. Because, we respect the freedom of others, and that is the reason for his 
        first vision of Freedom. India got its first vision of this in the Indian Rebellion in the year 1857, when we started the 
        war of Independence. It is this freedom that we must protect and nurture and build on.We have been a developing nation for 
        fifty years, and so it is time we see ourselves as a developed nation. In terms of GDP, we are among the top five nations 
        of the world. Our poverty levels are falling. Our achievements are being globally recognised today. Yet we lack the 
        self-confidence to see ourselves as a developed nation.India must stand up to the world. Unless India stands up to the world, 
        no one will respect us. Only strength respects strength. We must be strong not only as a military power but also as an 
        economic power. Both must go hand-in-hand.Dr.Kalam says that being the project director for India’s first satellite 
        launch vehicle, SLV3, was the first milestone in his career. Second was when Agni met its mission requirements in 1994. 
        Third came the partnership between DRDO and the Dept of Atomic Energy. Removing the pain of little boys and girls in hospital, 
        by replacing heavy metallic calipers weighing over 3-kg each with 300-gram calipers, was the fourth bliss or milestone of 
        his career"""

#tokinixing sentence
sentence=nltk.sent_tokenize(para)

#tokinixing words

words=nltk.word_tokenize(para)
print(words)

