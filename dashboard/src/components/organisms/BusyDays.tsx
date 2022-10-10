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

type DayData = {
    day: string;
    people: number;
}

type Props = {
    days: Array<DayData>
}

const BusyDays: React.FC <Props> = ({days}) => {
    const labels = ['M', 'T', 'W', 'T', 'F', 'S', 'S'];

    const data = {
        labels,
        datasets: [
          {
            data: days.map((item) => item.people),
            backgroundColor: '#d9d9d9',
            borderRadius: 10,
          },
        ],
    };
    return (
        <div className='h-[25rem] bg-zinc-100 rounded-lg p-6'>
            <Title title='Busy days'/>
            <div className='flex justify-center h-[400px] p-10'>
                <div className='h-64 w-[90%]'>
                    <Bar data={data} options={options}/>
                </div>
            </div>
        </div>
    );
};

export default BusyDays;