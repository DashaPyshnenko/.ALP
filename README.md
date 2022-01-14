# .ALP
# Задание
Из текста на русском языке выделить все предложения.
Для каждого предложения выполнить:
1) Выделить части речи и предположить структуру предложения
2) Взяв за основу одну из известных структур построить графическое представление предложения в нотации dot
Для всего текста - собрать граф всех предложений.
Программа может поддерживать 2-3 различных типовых структур.

# Описание работы:
Произвольный текст на русском языке делится на предложения.
C помощью библиотеки NLTK выполняем токенизацию по предложения и словам.
Выделяем части речи с помощью pymorphy2 и предполагаем структуры предложений с помощью парсера.
Отдельным файлом добавляем граф предложений всего текста в нотации DOT.
Программа может поддерживать 2-3 различных типовых структур.

# Наш текст: Наступило лето. В саду поспела смородина. Даша и Алиса собирают ее в ведерко. Мама будет варить варенье. Дети будут пить чай с вареньем.

# Вывод программы:
['наступило лето', ' в саду поспела смородина', ' даша и алиса собирают ее в ведерко', ' мама будет варить варенье', ' дети будут пить чай с вареньем', '']

[('наступило', 'JJ'), ('лето', 'NNP'), ('.', '.'), ('в', 'VB'), ('саду', 'JJ'), ('поспела', 'NNP'), ('смородина', 'NNP'), ('.', '.'), ('даша', 'VB'), ('и', 'JJ'),
 ('алиса', 'NNP'), ('собирают', 'NNP'), ('ее', 'NNP'), ('в', 'NNP'), ('ведерко', 'NNP'), ('.', '.'), ('мама', 'VB'), ('будет', 'JJ'), ('варить', 'NNP'), ('варенье', 'NNP'),
 ('.', '.'), ('дети', 'VB'), ('будут', 'JJ'), ('пить', 'NNP'), ('чай', 'NNP'), ('с', 'NNP'), ('вареньем', 'NNP'), ('.', '.')]
 
 {'наступило': OpencorporaTag('VERB,perf,intr neut,sing,past,indc'), 'лето': OpencorporaTag('NOUN,inan,neut,Sgtm sing,accs'), '.': OpencorporaTag('PNCT'), 
'в': OpencorporaTag('PREP'), 'саду': OpencorporaTag('NOUN,inan,masc sing,loc2'), 'поспела': OpencorporaTag('VERB,perf,intr femn,sing,past,indc'), 
'смородина': OpencorporaTag('NOUN,inan,femn sing,nomn'), 'даша': OpencorporaTag('NOUN,anim,femn,Name sing,nomn'), 'и': OpencorporaTag('CONJ'), 
'алиса': OpencorporaTag('NOUN,anim,femn,Name sing,nomn'), 'собирают': OpencorporaTag('VERB,impf,tran plur,3per,pres,indc'), 'ее': OpencorporaTag('NPRO,femn,3per,Anph sing,accs'),
 'ведерко': OpencorporaTag('NOUN,inan,neut sing,nomn'), 'мама': OpencorporaTag('NOUN,anim,femn sing,nomn'), 'будет': OpencorporaTag('VERB,impf,intr sing,3per,futr,indc'),
 'варить': OpencorporaTag('INFN,impf,tran'), 'варенье': OpencorporaTag('NOUN,inan,neut sing,nomn,V-be'), 'дети': OpencorporaTag('NOUN,anim,masc plur,nomn'), 
'будут': OpencorporaTag('VERB,impf,intr plur,3per,futr,indc'), 'пить': OpencorporaTag('INFN,impf,tran'), 'чай': OpencorporaTag('NOUN,inan,masc sing,nomn'),
 'с': OpencorporaTag('PREP'), 'вареньем': OpencorporaTag('NOUN,inan,neut sing,ablt,V-be')}
 
           S      
     ______|___    
    VP         NP 
    |          |   
    V          N  
    |          |   
наступило     лето
              S                   
          ____|______________      
         VP                  |    
      ___|__________         |     
     PP             |        NP   
  ___|___           |        |     
 P       N          V        N    
 |       |          |        |     
 в      саду     поспела смородина
                  S                        
       ___________|______                   
      |                  VP                
      |            ______|_______           
      NP          |      |       PP        
  ____|____       |      |    ___|_____     
 N    P    N      V      N   P         N   
 |    |    |      |      |   |         |    
даша  и  алиса собирают  ее  в      ведерко
            S                    
  __________|____                 
 |               VP              
 |      _________|_____           
 |     |               S         
 |     |          _____|_____     
 NP    |         VP          NP  
 |     |         |           |    
 N     V         V           N   
 |     |         |           |    
мама будет     варить     варенье
            S                       
  __________|____                    
 |               VP                 
 |      _________|___                
 |     |             S              
 |     |     ________|___            
 NP    |    VP           NP         
 |     |    |     _______|_____      
 N     V    V    N       P     N    
 |     |    |    |       |     |     
дети будут пить чай      с  вареньем

