DESTDIR ?= /usr

PREFIXBIN=$(DESTDIR)/bin
PREFIXLIB=$(DESTDIR)/lib/pyglparchis
PREFIXSHARE=$(DESTDIR)/share/pyglparchis 

install:
	echo "Instalando en ${DESTDIR}"
	pyuic4 ui/frmAbout.ui > ui/Ui_frmAbout.py
	pyuic4 ui/frmLanguage.ui > ui/Ui_frmLanguage.py
	pyuic4 ui/frmMain.ui > ui/Ui_frmMain.py
	pyuic4 ui/wdgUserPanel.ui > ui/Ui_wdgUserPanel.py
	pyrcc4 images/glparchis.qrc > images/glparchis_rc.py
	install -o root -d $(PREFIXBIN)
	install -o root -d $(PREFIXLIB)
	install -o root -d $(PREFIXSHARE)                                                      
	install -m 755 -o root glparchis.py $(PREFIXBIN)/pyglparchis
	install -m 644 -o root datos.py $(PREFIXLIB)                
	install -m 644 -o root ui/*.py $(PREFIXLIB)                
	install -m 644 -o root images/*.py $(PREFIXLIB)
	install -m 644 -o root LICENSE $(PREFIXSHARE)
	install -m 644 -o root images/ficharoja.png $(PREFIXLIB)

#	install -m 644 -o root po/es.mo $(PREFIXPO)/es/LC_MESSAGES/recovermypartition.mo

uninstall:
	rm $(PREFIXBIN)/pyglparchis
	rm -Rf $(PREFIXLIB)
	rm -Rf $(PREFIXSHARE)



