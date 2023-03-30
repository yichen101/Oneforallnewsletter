import classes from './MenuTab.module.css'
import { Link } from 'react-router-dom';

function MenuTab(props) {

    const scrollToSection = (sectionId) => {
        const section = document.getElementById(sectionId);
        if (section) {
          section.scrollIntoView({ behavior: 'smooth' });
        }
      };

    return (
        <div>
            {props.sections.map((section, i) => {
                return (
                    <div className={classes.column}>
                        <Link key={section.id}
                              to={`#${section.id}`}
                              onClick={() => scrollToSection(section.id)}
                              className={classes.text}>
                            {section.name}
                        </Link>
                    </div>
                )
            })}
        </div>
    )
}

export default MenuTab