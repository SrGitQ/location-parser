import React from 'react';
import { BasicInformation, Metrics, Charts, Competency } from './components';
import Place from './utils/types';

type Props = {
  place: Place | null;
};

const Layout2: React.FC <Props> = ({place}) => {
    return place ? (
        
      <div className="grid-rows-4">
        <BasicInformation place={place}/>
        <Metrics wordCloud={place.wordCloud} sentiment={place.sentiment} website={place.website} id={place.place_id}/>
        <Charts busyDays={place.busyDays} busyHours={place.busyHours}/>
        {/* <Competency competency={place.competency}/> */}
      </div>
    ) : (<></>)
}

export default Layout2;
