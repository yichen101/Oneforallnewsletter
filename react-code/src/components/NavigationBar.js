import {Link} from 'react-router-dom'
import classes from './NavigationBar.module.css'

function NavigationBar() {
    return (
        <div>
            <div>
                <Link to='/' className={classes.header}>
                    <h1>"One For All" Newsletter</h1>
                </Link>
            </div>
            <ul >
                <div className={classes.bar}>
                    <li>
                        <Link to='/financial-times'>
                            <img src="https://raw.githubusercontent.com/yichen101/Projectimages/main/images/ft_icon.jpg" alt='FT icon' className={classes.icon}/>
                        </Link> 
                    </li>
                    <li>
                        <Link to='/telegraph'>
                            <img src='https://raw.githubusercontent.com/yichen101/Projectimages/main/images/telegraph_icon.jpg' alt='Telegraph icon' className={classes.icon}/>
                        </Link>
                    </li>
                    <li>
                        <Link to='/fool'>
                            <img src='https://raw.githubusercontent.com/yichen101/Projectimages/main/images/fool_icon.jpg' alt='Fool icon' className={classes.icon}/>
                        </Link>
                    </li>
                    <li>
                        <Link to='/economist'>
                            <img src='https://raw.githubusercontent.com/yichen101/Projectimages/main/images/economist_icon.jpg' alt='Economist icon' className={classes.icon}/>
                        </Link>
                    </li>
                    <li>
                        <Link to='/wall-street-journal'>
                            <img src='https://raw.githubusercontent.com/yichen101/Projectimages/main/images/wsj_icon.jpg' alt='WSJ icon' className={classes.icon}/>
                        </Link>
                    </li>
                    <li>
                        <Link to='/tech-target'>
                            <img src='https://raw.githubusercontent.com/yichen101/Projectimages/main/images/tt_icon.jpg' alt='TT icon' className={classes.icon}/>
                        </Link>
                    </li>
                    <li>
                        <Link to='/spectator'>
                            <img src='https://raw.githubusercontent.com/yichen101/Projectimages/main/images/spectator_icon.jpg' alt='Spectator icon' className={classes.icon}/>
                        </Link>
                    </li>
                </div>
            </ul>
            
        </div>
    )


}

export default NavigationBar