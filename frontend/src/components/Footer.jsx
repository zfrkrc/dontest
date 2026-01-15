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
                                    <strong>İletişim</strong>
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
                                            <strong>Telefon:</strong> <a href="tel:05346636464" className="text-black">0534 663 64 64</a>
                                        </li>
                                        <li className="mbr-text item-wrap">
                                            <strong>Email:</strong> <a href="mailto:zafer@zaferkaraca.net" className="text-black">zafer@zaferkaraca.net</a>
                                        </li>
                                        <li className="mbr-text item-wrap">
                                            <strong>Adres:</strong> Ankara, Türkiye
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div className="col-md-12 col-lg-6">
                            <div className="text-wrapper">
                                <p className="mbr-text display-7">
                                    <strong>Zafer Karaca</strong> - Kişisel Web Sitesi ve Projeleri.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <section className="display-7" style={{ padding: '1rem', alignItems: 'center', justifyContent: 'center', display: 'flex', backgroundColor: '#f0f0f0' }}>
                <p style={{ margin: 0, textAlign: 'center' }} className="display-7">
                    © Copyright 2025 Zafer Karaca - All Rights Reserved
                </p>
            </section>
        </>
    );
};

export default Footer;
