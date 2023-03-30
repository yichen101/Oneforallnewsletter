import './App.css';
import {Route, Routes} from 'react-router-dom'
import NavigationBar from './components/NavigationBar';
import AllPage from './pages/All'
import FinancialTimesPage from './pages/FinancialTimes';
import TelegraphPage from './pages/Telegraph'
import EconomistPage from './pages/Economist'
import WallStreetJournalPage from './pages/WallStreetJournal'
import FoolPage from './pages/Fool'
import TechTargetPage from './pages/TechTarget'
import SpectatorPage from './pages/Spectator'


function App() {
  return (
    <div className='backgroundColor'>
      <NavigationBar/>
      <Routes>
        <Route path ='/' element = {<AllPage/>}/>
        <Route path ='/financial-times' element = {<FinancialTimesPage/>}/>
        <Route path ='/telegraph' element = {<TelegraphPage/>}/>
        <Route path ='/economist' element = {<EconomistPage/>}/>
        <Route path ='/wall-street-journal' element = {<WallStreetJournalPage/>}/>
        <Route path ='/fool' element = {<FoolPage/>}/>
        <Route path ='/tech-target' element = {<TechTargetPage/>}/>
        <Route path ='/spectator' element = {<SpectatorPage/>}/>
      </Routes>
    </div>
  );
}

export default App;