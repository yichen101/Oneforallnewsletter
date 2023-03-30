import classes from './All.module.css'
import Axios from 'axios';
import { useEffect, useState, useRef } from 'react';
import {Link} from 'react-router-dom'
import PageList from '../components/PageList';
import MenuTab from '../components/MenuTab';
import ScrollToTop from '../components/ScrollToTop';
import '../App.css';

function AllPage() {
  const [listOfArticles, setListOfArticles] = useState([])
  const [searchWord, setSearchWord] = useState("")
  const [showListOfArticles, setShowListOfArticles] = useState(false)
  const newsletterList = ["The Economist", // List of all pages of website
                          "The Motley Fool",
                          "Financial Times", 
                          "The Spectator",
                          "The Telegraph",
                          "Tech Target",
                          "Wall Street Journal"]
  
  useEffect (() => { //Pull all data
    Axios.get("https://news-firebase-8a2f0-default-rtdb.europe-west1.firebasedatabase.app/.json")
      .then((response) => {
        //console.log(response.data)
        setListOfArticles(response.data)
      })
  }, [])
  
  const checkSearchWord = function(word) { //Only display articles when search bar is not empty 
    if (word === "") {
      setShowListOfArticles(false)
    } else {
      setShowListOfArticles(true)
    }
  }

  const filteredArticles = {}
  const newsletterSectionList = [] //Create new json containing article information
  Object.keys(listOfArticles).forEach((newsletter, i) => {
    newsletterSectionList.push({"name": newsletterList[i], "id": newsletterList[i].toLowerCase()}) //Add newsletter name & ID to a list
    const articlesList = []
    Object.keys(listOfArticles[newsletter]).forEach((page, i) => {
      listOfArticles[newsletter][page]
      .filter(function(item){
        return item.title.toLowerCase().includes(searchWord.toLowerCase()) // Get items where the title matches search term
      })
      .forEach((item, i) => {
        if (articlesList.some((info) => info.title === item.title)) { //Remove duplicates titles
        } else {
          articlesList.push({"title": item.title, "link": item.link})
        }
      })
    })
    filteredArticles[newsletterList[i]] = articlesList
  })
  
  return (
    <div>
      <ScrollToTop/>
      <Link className={classes.link} to='/'>
          <h1 className={classes.mainHeader}>"One For All"<br/>
              Newsletter
          </h1>
      </Link>

      <div className={classes.mainSearchBarPosition}>
        <div className={classes.mainSearchBar}>
          <input type='text' placeholder='Search...' onChange={ (userInput) => {
            setSearchWord(userInput.target.value)
            checkSearchWord(userInput.target.value)
          }}/>
        </div>
      </div>

      <div id ='mainContent'>
        <div className='menuPosition'>
          {showListOfArticles && <MenuTab sections={newsletterSectionList}/>}
        </div>
        {showListOfArticles && <PageList pages={filteredArticles} sections={newsletterSectionList}/>}
      </div>
    </div>
  );
}

export default AllPage;