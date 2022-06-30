import pandas as pd

df = pd.read_csv('Q-A.csv')

#1. Index answer
answer_file = {}
answer_file['answerId'] = []
answer_file['answerFile'] = []
answer_file['answeredBy'] = []
for i, file in enumerate(df['Talk Name']):
    answer_file['answerId'].append('meta_ans_'+str(i).zfill(3))
    answer_file['answerFile'].append(file[:-3]+'sph')
    answer_file['answeredBy'].append('meta_ted')

answer_file = pd.DataFrame(answer_file)
answer_file.to_csv('answer_file.csv', index=False)


#print(answer_file[answer_file['answerFile'] == '911Mothers_2010W.sph']['answerId'][0])
#2. Index question
question_file = {}
question_file['questionId'] = []
question_file['questionContent'] = []
question_file['answerId'] = []
question_file['answerFile'] = []
question_file['postedBy'] = []
question_file['hashtag1'] = []
question_file['hashtag2'] = []
question_file['hashtag3'] = []
question_file['category'] = []
question_file['questionStatus'] = []
for i, row in df.iterrows():
    for j in range(3):
        question_file['questionId'].append('meta_qn_'+str(i*3+j).zfill(3))
        question_file['questionContent'].append(row['Question '+str(j+1)])
        question_file['answerId'].append([answer_file[answer_file['answerFile'] == (row['Talk Name'][:-3]+'sph')]['answerId'][i]])
        question_file['answerFile'].append([row['Talk Name'][:-3]+'sph'])
        question_file['postedBy'].append('meta_ted')
        question_file['hashtag1'].append('')
        question_file['hashtag2'].append('')
        question_file['hashtag3'].append('')
        question_file['category'].append('')
        question_file['questionStatus'].append('Answered')

question_file = pd.DataFrame(question_file)
question_file.to_csv('question_file.csv', index=False)
#print(answer_file.columns.values.tolist())
