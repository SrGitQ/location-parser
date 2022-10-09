import React from 'react';
import { RBox, MBox } from './boxes';

const BasicInformation: React.FC = () => {
	return (
		<div className='grid grid-cols-2 bg-color-red m-6 gap-6'>
			<div className='grid gap-6'>
				<RBox>
					basic information
				</RBox>
				<RBox>
					rating
				</RBox>
			</div>
			<MBox>
				map
			</MBox>
		</div>
	);
};

export default BasicInformation;