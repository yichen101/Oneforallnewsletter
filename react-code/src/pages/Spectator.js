import Axios from 'axios';
import { useEffect, useState } from 'react';
import classes from './Spectator.module.css'
import '../App.css'
import PageList from '../components/PageList';
import MenuTab from '../components/MenuTab'
import ScrollToTop from '../components/ScrollToTop';


function SpectatorPage() {
  const [listOfArticles, setListOfArticles] = useState([])
  const [searchWord, setSearchWord] = useState("")

  //Pull Spectator data
  useEffect (() => {
    Axios.get("ENTER YOUR API")
      .then((response) => {
        //console.log(response)
        setListOfArticles(response.data)
      })
  }, [])

  //Get titles/links that are in the search term
  let pageSectionList = []
  const filteredArticles = Object.keys(listOfArticles).map(page => {
    pageSectionList.push({"name": page.slice(16), "id": page.slice(16).toLowerCase()}) //Add page name & ID to a list
    return (
      Object.keys(listOfArticles[page])
      .filter(function(item){
        return listOfArticles[page][item].title.toLowerCase().includes(searchWord.toLowerCase()) // Get items where the title matches search term
      })
      .map(function (item) { // Return each filtered title/link
        return {
          "title":[listOfArticles[page][item].title], 
          "link" :[listOfArticles[page][item].link]
        }
      })
    )
  })
  // New dictionary to convert data back into original format 
  let newFilteredArticles = {}
  for (let i=0; i<pageSectionList.length; i++) {
    newFilteredArticles[pageSectionList[i].name] = filteredArticles[i]
  }

  return (
    <div className={classes.backgroundColor}>
      <ScrollToTop/>
      <img src='https://raw.githubusercontent.com/yichen101/Projectimages/main/images/spectator_banners.jpg' alt='Spectator logo' className={classes.img}/>
        <div id ='mainContent'>
          <div className='menuPosition'>
            <MenuTab sections={pageSectionList}/>
          </div>
          
          <PageList pages={newFilteredArticles} sections={pageSectionList}/>
          
          <div className='searchBarPosition'>
            <div className='searchBar'>
              <input type='text' placeholder='Search...' onChange={ (userInput) => {
                setSearchWord(userInput.target.value)
              }}/>
            </div>
          </div>
        </div>
    </div>
  );
}

export default SpectatorPage;
