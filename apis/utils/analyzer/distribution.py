def popular_times_analyzer(hours:dict)->tuple:
	aux_data = []
	for popular_t in hours:
		day = popular_t['day']
		#making the time variable given the dict structure 
		day = {'day':day, 'time':[]}
		for item in popular_t['popular_times']:
			try:
				hour = item['hour']
				percentage = item['percentage']
			except:
				pass
			day['time'].append({'hour':hour,'percentage':percentage})
		aux_data.append(day)

	aux_hours = {hour:0 for hour in range(1,25)}
	aux_days = {day:0 for day in range(1,8)}

	for day in aux_data:
		general = 0
		for hour in day['time']:
			try:
				time = hour['hour']
				percentage = hour['percentage']
				general += percentage
				if percentage > aux_hours[time]:
					aux_hours[time] = percentage
			except:
				pass
		aux_days[day['day']] = general
	

	parsed_hours = {'hours':[]}
	parsed_days = {'days':[]}
	for hour in aux_hours:
		parsed_hours['hours'].append({'hour':f'{hour}','people':aux_hours[hour]})
	days = {1:'M', 2:'T', 3:'W', 4:'T', 5:'F', 6:'S', 7:'S'}

	for day in aux_days:
		parsed_days['days'].append({'day':f'{days[day]}','people':aux_days[day]})
	return parsed_hours, parsed_days
