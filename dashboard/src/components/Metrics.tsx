import React from 'react';
import { RBox, MBox } from './boxes';
import { Title } from './text';

const Metrics: React.FC = () => {
  return (
		<div className='grid grid-cols-2 bg-color-red m-6 gap-6'>
			<MBox>
				<Title title='People says'/>
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