import React from 'react';
import { RBox, MBox } from './boxes';
import { Title } from './text';

const BasicInformation: React.FC = () => {
	return (
		<div className='grid grid-cols-2 bg-color-red m-6 gap-6'>
			<div className='grid gap-6'>
				<RBox>
					basic information
				</RBox>
				<RBox>
					<Title title='Rating'/>
				</RBox>
			</div>
			<MBox>
				<Title title='Route'/>
			</MBox>
		</div>
	);
};

export default BasicInformation;