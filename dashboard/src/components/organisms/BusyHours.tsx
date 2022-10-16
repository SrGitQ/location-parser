import React from 'react';
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
    animation: {
        duration: 0,
    },
    maintainAspectRatio: false
};

type HourTendency = {
	hour: string;
	people: number;
}

type BusyHours = {
	hours: HourTendency[];
}

type Props = {
    busyHours: BusyHours | null;
}

const BusyHours: React.FC <Props> = ({busyHours}) => {
    const labels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'];

    const data = {
        labels,
        datasets: [
          {
            data: busyHours?.hours.map((item) => item.people),
            backgroundColor: '#d9d9d9',
            borderRadius: 4,
          },
        ],
    };
    return (
        <div className='h-[25rem] bg-zinc-100 rounded-lg p-6'>
            <Title title='Busy hours'/>
            <div className='flex justify-center h-[400px] p-10'>
                <div className='h-64 w-[90%]'>
                    <Bar data={data} options={options}/>
                </div>
            </div>
        </div>
    );
};

export default BusyHours;
