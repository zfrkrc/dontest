import React from 'react';

const Footer = () => {
    return (
        <>
            <section data-bs-version="5.1" className="contacts02 map1 cid-uSrJKocEPl" id="contacts-2-uSrJKocEPl">
                <div className="container">
                    <div className="row justify-content-center">
                        <div className="col-12 content-head">
                            <div className="mbr-section-head mb-5">
                                <h3 className="mbr-section-title mbr-fonts-style align-center mb-0 display-2">
                                    <strong>İletişim Bilgileri</strong>
                                </h3>
                            </div>
                        </div>
                    </div>
                    <div className="row justify-content-center">
                        <div className="card col-12 col-md-12 col-lg-6">
                            <div className="card-wrapper">
                                <div className="text-wrapper">
                                    <ul className="list mbr-fonts-style display-7">
                                        <li className="mbr-text item-wrap">
                                            Telefon: <a href="tel:+90 555 123 45 67" className="text-black">+90 534&nbsp;</a>663 64 64
                                        </li>
                                        <li className="mbr-text item-wrap">
                                            WhatsApp: <a href="tel:+90 555 123 45 67" className="text-black">+90 5</a>34 663 64 64
                                        </li>
                                        <li className="mbr-text item-wrap">
                                            E-posta: <a href="mailto:info@teknolojia.com" className="text-black">zafer@</a>zaferkaraca.net
                                        </li>
                                        <li className="mbr-text item-wrap">
                                            <span style={{ fontSize: '1.4rem' }}>
                                                Çalışma Saatleri: Hafta İçi: 09:00 - 18:00
                                            </span>
                                            <br />
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div className="map-wrapper col-md-12 col-lg-6">
                            <div className="google-map">
                                <iframe
                                    frameBorder="0"
                                    style={{ border: 0 }}
                                    src="https://www.google.com/maps/embed/v1/place?key=AIzaSyCt1265A4qvZy9HKUeA8J15AOC4SrCyZe4&amp;q=Istanbul%20Turkey"
                                    allowFullScreen=""
                                ></iframe>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <section className="display-7" style={{ padding: 0, alignItems: 'center', justifyContent: 'center', flexWrap: 'wrap', alignContent: 'center', display: 'flex', position: 'relative', height: '4rem' }}>
                <a href="https://zaferkaraca.net" style={{ flex: '1 1', height: '4rem', position: 'absolute', width: '100%', zIndex: 1 }}>
                    <img alt="" style={{ height: '4rem' }} src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" />
                </a>
                <p style={{ margin: 0, textAlign: 'center' }} className="display-7">&#8204;</p>
                <a style={{ zIndex: 1 }} href="https://zaferkaraca.net">ZK</a>
            </section>
        </>
    );
};

export default Footer;
