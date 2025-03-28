import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Explore Core+ System 🏗️
          </Link>
          <Link
            className="button button--outline button--lg"
            to="/product-catalog">
            View Products 📋
          </Link>
        </div>
      </div>
    </header>
  );
}

function FeatureList() {
  return (
    <div className="container">
      <div className="row">
        <div className="col col--4">
          <div className={styles.feature}>
            <div className={styles.featureIcon}>🏗️</div>
            <h2>Advanced Panel System</h2>
            <p>High-performance SIP construction with pre-integrated utilities and factory-controlled quality.</p>
            <Link to="/docs/panels">Learn more →</Link>
          </div>
        </div>
        <div className="col col--4">
          <div className={styles.feature}>
            <div className={styles.featureIcon}>⚡</div>
            <h2>Quick Assembly</h2>
            <p>4-day standard assembly time with minimal equipment requirements and step-by-step guidance.</p>
            <Link to="/docs/assembly-guide">View guide →</Link>
          </div>
        </div>
        <div className="col col--4">
          <div className={styles.feature}>
            <div className={styles.featureIcon}>💰</div>
            <h2>Cost-Effective</h2>
            <p>30% lower than traditional construction with reduced labor costs and minimal waste.</p>
            <Link to="/cost-calculator">Calculate costs →</Link>
          </div>
        </div>
      </div>
      <div className="row">
        <div className="col col--4">
          <div className={styles.feature}>
            <div className={styles.featureIcon}>🛡️</div>
            <h2>Military Grade</h2>
            <p>UL 752 Level 3 ballistic protection and EI50 fire resistance rating available.</p>
            <Link to="/product-catalog#military-grade-panel-systems">View specs →</Link>
          </div>
        </div>
        <div className="col col--4">
          <div className={styles.feature}>
            <div className={styles.featureIcon}>🌡️</div>
            <h2>Fire Resistant</h2>
            <p>EI50 fire resistance rating with mineral wool core and intumescent coating.</p>
            <Link to="/product-catalog#fire-resistant-panel-systems">Learn more →</Link>
          </div>
        </div>
        <div className="col col--4">
          <div className={styles.feature}>
            <div className={styles.featureIcon}>🌍</div>
            <h2>Sustainable</h2>
            <p>Energy efficient design with recyclable materials and minimal carbon footprint.</p>
            <Link to="/docs/technical-specs#sustainability">View details →</Link>
          </div>
        </div>
      </div>
    </div>
  );
}

function CallToAction() {
  return (
    <div className={styles.cta}>
      <div className="container">
        <div className="row">
          <div className="col col--8">
            <h2>Ready to Transform Your Construction Project?</h2>
            <p>Get started with Core+ modular construction system today.</p>
          </div>
          <div className="col col--4">
            <div className={styles.ctaButtons}>
              <Link
                className="button button--primary button--lg"
                to="/docs/intro">
                Get Started
              </Link>
              <Link
                className="button button--outline button--lg"
                to="/contact">
                Contact Sales
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={siteConfig.title}
      description="Advanced panelized construction system with military-grade and fire-resistant options">
      <HomepageHeader />
      <main className={styles.main}>
        <FeatureList />
        <CallToAction />
      </main>
    </Layout>
  );
}
