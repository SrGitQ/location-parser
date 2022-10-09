import React from 'react';
import { PeopleSays, HeadsUp, Visitor } from './organisms';

const words = [
	{
		text: 'told',
	  	value: 64,
	},
	{
		text: 'mistake',
	  	value: 11,
	},
	{
		text: 'thought',
	  	value: 16,
	},
	{
		text: 'bad',
	  	value: 17,
	},
  ]

const Metrics: React.FC = () => {
  return (
		<div className='grid grid-cols-2 bg-color-red m-6 gap-6'>
			<PeopleSays words={words}/>
			<div className='grid gap-6'>
				<HeadsUp qal={[20, 40, 30]}/>
				<Visitor />
			</div>
		</div>
  );
};

export default Metrics;