import React from 'react';
import { RBox, MBox } from './boxes';
import { Title } from './text';
import ReactWordcloud from 'react-wordcloud';

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

const options:any = {
	rotationAngles : [0, 0],
	colors: ['#b7b9bc'],
	fontFamily: 'Arial Black',
	rotations: 1,
	enableOptimizations: false,
	fontSizes: [12, 40],
	fontWeight: 'bold',
	padding: 1,
	deterministic: true,
};
const size = [600, 400];
  

const Metrics: React.FC = () => {
  return (
		<div className='grid grid-cols-2 bg-color-red m-6 gap-6'>
			<MBox>
				<Title title='People says'/>
				<ReactWordcloud
					options={options}
					words={words} 
				/>
			</MBox>
			<div className='grid gap-6'>
				<RBox>
					<Title title='People think'/>
				</RBox>
				<RBox>
					QR
				</RBox>
			</div>
		</div>
  );
};

export default Metrics;