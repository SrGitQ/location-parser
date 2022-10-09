import React from 'react';
import { MBox } from './boxes';
import { BusyDays, BusyHours } from './organisms';
import { Title } from './text';

const busy_day_data = [
	{day: 'M',people: 10,},
	{day: 'T',people: 20,},
	{day: 'W',people: 30,},
	{day: 'T',people: 10,},
	{day: 'F',people: 20,},
	{day: 'S',people: 30,},
	{day: 'S',people: 40,},
]

const busy_hours_data = [
	{hour: '1',people: 10,},
	{hour: '2',people: 20,},
	{hour: '3',people: 30,},
	{hour: '4',people: 30,},
	{hour: '5',people: 50,},
	{hour: '6',people: 60,},
	{hour: '7',people: 20,},
	{hour: '8',people: 10,},
	{hour: '9',people: 70,},
	{hour: '10',people: 100,},
	{hour: '11',people: 10,},
	{hour: '12',people: 20,},
	{hour: '13',people: 30,},
	{hour: '14',people: 50,},
	{hour: '15',people: 50,},
	{hour: '16',people: 60,},
	{hour: '17',people: 70,},
	{hour: '18',people: 20,},
	{hour: '19',people: 58,},
	{hour: '20',people: 40,},
	{hour: '21',people: 10,},
	{hour: '22',people: 20,},
	{hour: '23',people: 30,},
	{hour: '24',people: 40,},
]

const Charts: React.FC = () => {
	return (
		<div className='grid grid-cols-2 bg-color-red m-6 gap-6'>
			<BusyDays days={busy_day_data}/>
			<BusyHours hours={busy_hours_data}/>
		</div>
	);
};

export default Charts;