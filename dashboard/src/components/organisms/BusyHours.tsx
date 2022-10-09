import React from 'react';
import { MBox } from '../boxes';
import { Title } from '../text';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Tooltip,
);

export const options = {
    responsive: true,
    scales: {
        x: {
            grid: {
                display: false,
            },
        },
        y: {
            grid: {
                display: false,
            },
            ticks: {
                display: false,
            },
        },
    },
    maintainAspectRatio: false
};

type HourData = {
    hour: string;
    people: number;
}

type Props = {
    hours: Array<HourData>
}

const BusyHours: React.FC <Props> = ({hours}) => {
    const labels = ['8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'];

    const data = {
        labels,
        datasets: [
          {
            data: hours.map((item) => item.people),
            backgroundColor: '#b7b9bc',
            borderRadius: 4,
          },
        ],
    };
    return (
        <MBox>
            <Title title='Busy hours'/>
            <div className='flex justify-center h-[400px] p-10'>
                <div className='h-80 w-[90%]'>
                    <Bar data={data} options={options}/>
                </div>
            </div>
        </MBox>
    );
};

export default BusyHours;