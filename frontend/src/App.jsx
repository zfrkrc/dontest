import React from 'react'
import Navbar from './components/Navbar'
import Footer from './components/Footer'

function App() {
  return (
    <>
      <Navbar />

      {/* Hero Section */}
      <section data-bs-version="5.1" className="header18 cid-uSrJKo5xsn mbr-fullscreen mbr-parallax-background" id="hero-16-uSrJKo5xsn">
        <div className="mbr-overlay" style={{ opacity: 0.5, backgroundColor: 'rgb(0, 0, 0)' }}></div>
        <div className="container-fluid">
          <div className="row">
            <div className="content-wrap col-12 col-md-12">
              <h1 className="mbr-section-title mbr-fonts-style mbr-white mb-4 display-1">
                <strong>Teknoloji Partneri</strong></h1>
              <p className="mbr-fonts-style mbr-text mbr-white mb-4 display-7">Sistem ürünleri, sunucular ve depolama çözümleriyle dijital gücünüzü artırın.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section data-bs-version="5.1" className="people07 cid-uSrJKo6yl4" id="testimonials-8-uSrJKo6yl4">
        <div className="container">
          <div className="row justify-content-center">
            <div className="col-md-12 col-lg-8">
              <p className="card-text mbr-fonts-style display-5">Sistemlerinizin performans ve güvenlik beklentilerini anlayıp tasarlamamız için iletişime geçebilirsiniz.</p>
              <div className="img-wrapper mt-3 justify-content-center">
                <img src="/assets/images/screenshot-20250201-170402-instagram-240x240.webp" alt="" data-slide-to="0" data-bs-slide-to="0" />
              </div>
              <p className="card-title mbr-fonts-style mt-3 display-7">
                <strong>Zafer KARACA , Matematikçi</strong></p>
            </div>
          </div>
        </div>
      </section>

      {/* Video Section (Placeholder as in source) */}
      <section data-bs-version="5.1" className="header18 cid-uSrJKo73AL mbr-fullscreen" id="video-5-uSrJKo73AL">
        <div className="mbr-overlay" style={{ opacity: 0, backgroundColor: 'rgb(0, 0, 0)' }}></div>
        <div className="container">
          <div className="row">
          </div>
        </div>
      </section>

      {/* Call to Action Section */}
      <section data-bs-version="5.1" className="header14 cid-uSrJKo7xHR mbr-fullscreen" id="call-to-action-9-uSrJKo7xHR">
        <div className="container">
          <div className="row justify-content-center">
            <div className="card col-12 col-md-12 col-lg-12">
              <div className="card-wrapper">
                <div className="card-box align-center">
                  <h1 className="card-title mbr-fonts-style mb-4 display-1"><strong>Adım Adım Teknoloji</strong></h1>
                  <p className="mbr-text mbr-fonts-style mb-4 display-7">İnovatif çözümlerimizle işinizi ileriye taşıyın. Hemen harekete geçin!</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Slider Section */}
      <section data-bs-version="5.1" className="features017 mbr-embla cid-uSrJKo86Hs" id="features-17-uSrJKo86Hs">
        <div className="position-relative">
          <div className="container-fluid">
            <div className="row justify-content-center">
              <div className="col-12 content-head">
                <div className="mbr-section-head mb-5">
                  <h4 className="mbr-section-title mbr-fonts-style align-center mb-0 display-2">
                    <strong>Öne Çıkanlar</strong>
                  </h4>
                  <h5 className="mbr-section-subtitle mbr-fonts-style align-center mb-0 mt-4 display-7">Teknolojinin Zirvesi</h5>
                </div>
              </div>
            </div>
          </div>

          <div className="embla" data-skip-snaps="true" data-align="center" data-contain-scroll="trimSnaps" data-auto-play-interval="5" data-draggable="true">
            <div className="embla__viewport container-fluid">
              <div className="embla__container">
                <div className="embla__slide slider-image item active" style={{ marginLeft: '4rem', marginRight: '4rem' }}>
                  <div className="slide-content">
                    <div className="item-img">
                      <div className="item-wrapper">
                        <img src="/assets/images/photo-1584169417032-d34e8d805e8b.webp" alt="ZK" title="" data-slide-to="1" data-bs-slide-to="1" />
                      </div>
                    </div>
                    <div className="item-content">
                      <h5 className="item-title mbr-fonts-style display-5">
                        <strong>Sunucular</strong>
                      </h5>
                      <p className="mbr-text mbr-fonts-style mt-3 display-7">Güçlü sunucularımızla kesintisiz hizmet.</p>
                    </div>
                  </div>
                </div>
                <div className="embla__slide slider-image item" style={{ marginLeft: '4rem', marginRight: '4rem' }}>
                  <div className="slide-content">
                    <div className="item-img">
                      <div className="item-wrapper">
                        <img src="/assets/images/photo-1683322499436-f4383dd59f5a.webp" alt="ZK" title="" data-slide-to="2" data-bs-slide-to="2" />
                      </div>
                    </div>
                    <div className="item-content">
                      <h5 className="item-title mbr-fonts-style display-5">
                        <strong>Depolama</strong>
                      </h5>
                      <p className="mbr-text mbr-fonts-style mt-3 display-7">Gelişmiş depolama sistemleriyle verilerinizi koruyun.</p>
                    </div>
                  </div>
                </div>
                <div className="embla__slide slider-image item" style={{ marginLeft: '4rem', marginRight: '4rem' }}>
                  <div className="slide-content">
                    <div className="item-img">
                      <div className="item-wrapper">
                        <img src="/assets/images/photo-1667372459607-2cfe842fdc4b.webp" alt="ZK" title="" data-slide-to="3" data-bs-slide-to="3" />
                      </div>
                    </div>
                    <div className="item-content">
                      <h5 className="item-title mbr-fonts-style display-5">
                        <strong>Sistemler</strong>
                      </h5>
                      <p className="mbr-text mbr-fonts-style mt-3 display-7">Windows ve Linux sistemleriyle esnek çözümler.</p>
                    </div>
                  </div>
                </div>
                <div className="embla__slide slider-image item" style={{ marginLeft: '4rem', marginRight: '4rem' }}>
                  <div className="slide-content">
                    <div className="item-img">
                      <div className="item-wrapper">
                        <img src="/assets/images/photo-1573164713988-8665fc963095.webp" alt="ZK" title="" data-slide-to="4" data-bs-slide-to="4" />
                      </div>
                    </div>
                    <div className="item-content">
                      <h5 className="item-title mbr-fonts-style display-5">
                        <strong>Sanallaştırma</strong>
                      </h5>
                      <p className="mbr-text mbr-fonts-style mt-3 display-7">Proxmox ile sanallaştırma altyapınızı optimize edin.</p>
                    </div>
                  </div>
                </div>
                <div className="embla__slide slider-image item" style={{ marginLeft: '4rem', marginRight: '4rem' }}>
                  <div className="slide-content">
                    <div className="item-img">
                      <div className="item-wrapper">
                        <img src="/assets/images/photo-1680691257251-5fead813b73e.webp" alt="ZK" title="" data-slide-to="5" data-bs-slide-to="5" />
                      </div>
                    </div>
                    <div className="item-content">
                      <h5 className="item-title mbr-fonts-style display-5">
                        <strong>Güvenlik</strong>
                      </h5>
                      <p className="mbr-text mbr-fonts-style mt-3 display-7">Güvenlik duvarları ve testlerle ağınızı güvence altına alın.</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <button className="embla__button embla__button--prev">
              <span className="mobi-mbri mobi-mbri-arrow-prev mbr-iconfont" aria-hidden="true"></span>
              <span className="sr-only visually-hidden visually-hidden">Previous</span>
            </button>
            <button className="embla__button embla__button--next">
              <span className="mobi-mbri mobi-mbri-arrow-next mbr-iconfont" aria-hidden="true"></span>
              <span className="sr-only visually-hidden visually-hidden">Next</span>
            </button>
          </div>
        </div>
      </section>

      {/* Features Grid Section */}
      <section data-bs-version="5.1" className="features5 cid-uSrJKoa50J" id="features-22-uSrJKoa50J">
        <div className="container">
          <div className="row mb-5 justify-content-center">
            <div className="col-12 content-head">
              <h3 className="mbr-section-title mbr-fonts-style align-center mb-0 display-2">
                <strong>Veri Merkezi Çözümleri</strong>
              </h3>
            </div>
          </div>
          <div className="row">
            <div className="item features-without-image col-12 col-md-6 col-lg-4 item-mb">
              <div className="item-wrapper">
                <div className="card-box align-left">
                  <h5 className="card-title mbr-fonts-style display-5">
                    <strong>Sunucu &amp; Depolama</strong>
                  </h5>
                  <p className="card-text mbr-fonts-style display-7">Sunucular, depolama sistemleri ve ağ donanımları ile veri merkezleri için güçlü çözümler.</p>
                </div>
              </div>
            </div>
            <div className="item features-without-image col-12 col-md-6 col-lg-4 item-mb">
              <div className="item-wrapper">
                <div className="card-box align-left">
                  <h5 className="card-title mbr-fonts-style display-5">
                    <strong>İşletim Sistemleri</strong>
                  </h5>
                  <p className="card-text mbr-fonts-style display-7">Windows, Linux ve açık kaynak işletim sistemleri ile esnek altyapılar.</p>
                </div>
              </div>
            </div>
            <div className="item features-without-image col-12 col-md-6 col-lg-4 item-mb">
              <div className="item-wrapper">
                <div className="card-box align-left">
                  <h5 className="card-title mbr-fonts-style display-5">
                    <strong>Güvenlik &amp; Sanallaştırma</strong>
                  </h5>
                  <p className="card-text mbr-fonts-style display-7">Sanallaştırma, güvenlik duvarları ve sızma testleri ile üst düzey güvenlik.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </>
  )
}

export default App
