# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2.1 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PySPED - Bibliotecas Python para o
#          SPED - Sistema Público de Escrituração Digital
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Library General Public License,
# publicada pela Free Software Foundation, em sua versão 2.1 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Library General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Library General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#

from __future__ import division, print_function, unicode_literals

from os.path import abspath, dirname
from datetime import datetime
from pysped.nfe import ProcessadorNFe
from pysped.nfe.webservices_flags import (UF_CODIGO,
                                          WS_NFE_CONSULTA_RECIBO)


from pysped.nfe.leiaute import Det_310,NFe_310


FILE_DIR = abspath(dirname(__file__))


if __name__ == '__main__':
    p = ProcessadorNFe()
    p.versao              = '3.10'
    p.estado              = 'RS'
    #p.certificado.arquivo = 'certificado.pfx'
    #p.certificado.senha   = 'senha'

    #
    # arquivo 'certificado_caminho.txt' deve conter o caminho para o 'certificado.pfx'
    #
    p.certificado.arquivo = open('/certificado_caminho.txt').read().strip()

    #
    # arquivo 'certificado_senha.txt' deve conter a senha para o 'certificado.pfx'
    #
    p.certificado.senha   = open('/certificado_senha.txt').read().strip()

    p.salva_arquivos      = True
    p.contingencia_SCAN   = False
    p.caminho = ''

    #
    # Instancia uma NF-e
    #
    n = NFe_310()

    #
    # Identificação da NF-e
    #
    n.infNFe.ide.cUF.valor     = UF_CODIGO['RS']
    n.infNFe.ide.natOp.valor   = 'Venda de produto no website'
    n.infNFe.ide.indPag.valor  = 0
    n.infNFe.ide.serie.valor   = 1
    n.infNFe.ide.nNF.valor     = 171769
    n.infNFe.ide.dEmi.valor    = datetime.now()
    n.infNFe.ide.dSaiEnt.valor = datetime.now()
    n.infNFe.ide.cMunFG.valor  = 4321501
    n.infNFe.ide.tpImp.valor   = 1
    n.infNFe.ide.tpEmis.valor  = 1
    n.infNFe.ide.indPag.valor  = 1
    n.infNFe.ide.finNFe.valor  = 1
    n.infNFe.ide.procEmi.valor = 0
    n.infNFe.ide.verProc.valor = 'Sistema MiniLoja '

    #
    # Emitente
    #
    n.infNFe.emit.CNPJ.valor  = u'04494718000132'
    n.infNFe.emit.xNome.valor = 'AUTODIDATA EDITORA LTDA ME'
    n.infNFe.emit.xFant.valor = 'Autodidata Editora'
    n.infNFe.emit.enderEmit.xLgr.valor    = 'Travessa Macahdo'
    n.infNFe.emit.enderEmit.nro.valor     = '11'
    n.infNFe.emit.enderEmit.xCpl.valor    = ''
    n.infNFe.emit.enderEmit.xBairro.valor = 'Igra Sul'
    n.infNFe.emit.enderEmit.cMun.valor    = '4321501'
    n.infNFe.emit.enderEmit.xMun.valor    = 'Torres'
    n.infNFe.emit.enderEmit.UF.valor      = 'RS'
    n.infNFe.emit.enderEmit.CEP.valor     = '95560000'
    #n.infNFe.emit.enderEmit.cPais.valor   = '1058'
    #n.infNFe.emit.enderEmit.xPais.valor   = 'Brasil'
    n.infNFe.emit.enderEmit.fone.valor    = '5136261743'
    n.infNFe.emit.IE.valor = '1440100206'
    #
    # Regime tributário
    #
    n.infNFe.emit.CRT.valor = 1

    #
    # Destinatário
    #
    n.infNFe.dest.CPF.valor  = '62947729072'
    n.infNFe.dest.xNome.valor = 'Lauro Cesar'
    n.infNFe.dest.enderDest.xLgr.valor    = 'Jose Osorio'
    n.infNFe.dest.enderDest.nro.valor     = '14'
    n.infNFe.dest.enderDest.xCpl.valor    = ''
    n.infNFe.dest.enderDest.xBairro.valor = 'Jd. Santa Rosália'
    n.infNFe.dest.enderDest.cMun.valor    = '3552205'
    n.infNFe.dest.enderDest.xMun.valor    = 'Sorocaba'
    n.infNFe.dest.enderDest.UF.valor      = 'SP'
    n.infNFe.dest.enderDest.CEP.valor     = '18095360'
    #n.infNFe.dest.enderDest.cPais.valor   = '1058'
    #n.infNFe.dest.enderDest.xPais.valor   = 'Brasil'
    n.infNFe.dest.enderDest.fone.valor    = '1534110602'
    #n.infNFe.dest.IE.valor = '111111111111'
    #
    # Emeio
    #
    n.infNFe.dest.email.valor = 'lauro@hostcert.com.br'

    #
    # Detalhe
    #
    d1 = Det_310()

    d1.nItem.valor = 1
    d1.prod.cProd.valor    = 'código do produto'
    d1.prod.cEAN.valor     = ''
    d1.prod.xProd.valor    = 'Descrição do produto'
    d1.prod.NCM.valor      = '49019900'
    d1.prod.EXTIPI.valor   = ''
    d1.prod.CFOP.valor     = '5101'
    d1.prod.uCom.valor     = 'UN'
    d1.prod.qCom.valor     = '1.00'
    d1.prod.vUnCom.valor   = '1000.00'
    d1.prod.vProd.valor    = '1000.00'
    d1.prod.cEANTrib.valor = ''
    d1.prod.uTrib.valor    = d1.prod.uCom.valor
    d1.prod.qTrib.valor    = d1.prod.qCom.valor
    d1.prod.vUnTrib.valor  = d1.prod.vUnCom.valor
    d1.prod.vFrete.valor   = '0.00'
    d1.prod.vSeg.valor     = '0.00'
    d1.prod.vDesc.valor    = '0.00'
    d1.prod.vOutro.valor   = '0.00'
    #
    # Produto entra no total da NF-e
    #
    d1.prod.indTot.valor   = 1

    #
    # Impostos
    #
    d1.imposto.ICMS.CST.valor   = '00'
    d1.imposto.ICMS.modBC.valor = 3
    d1.imposto.ICMS.vBC.valor   = '0.00'
    d1.imposto.ICMS.pICMS.valor = '0.00'
    d1.imposto.ICMS.vICMS.valor = '0.00'

    d1.imposto.IPI.CST.valor    = '0.00'
    d1.imposto.IPI.vBC.valor    = '1000.00'
    d1.imposto.IPI.pIPI.valor   = '0.00'
    d1.imposto.IPI.vIPI.valor   = '0.00'

    d1.imposto.PIS.CST.valor    = '01'
    d1.imposto.PIS.vBC.valor    = '1000.00'
    d1.imposto.PIS.pPIS.valor   = '0.0'
    d1.imposto.PIS.vPIS.valor   = '0.0'

    d1.imposto.COFINS.CST.valor    = '06'
    d1.imposto.COFINS.vBC.valor    = '1000.00'
    d1.imposto.COFINS.pCOFINS.valor   = '0.00'
    d1.imposto.COFINS.vCOFINS.valor   = '0.00'

    #
    # Os primeiros 188 caracteres desta string
    # são todos os caracteres válidos em tags da NF-e
    #
    d1.infAdProd.valor = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿À'

    #
    # Inclui o detalhe na NF-e
    #
    n.infNFe.det.append(d1)

    #
    # Totais
    #
    n.infNFe.total.ICMSTot.vBC.valor     = '0.00'
    n.infNFe.total.ICMSTot.vICMS.valor   = '0.00'
    n.infNFe.total.ICMSTot.vBCST.valor   = '0.00'
    n.infNFe.total.ICMSTot.vST.valor     = '0.00'
    n.infNFe.total.ICMSTot.vProd.valor   = '1000.00'
    n.infNFe.total.ICMSTot.vFrete.valor  = '0.00'
    n.infNFe.total.ICMSTot.vSeg.valor    = '0.00'
    n.infNFe.total.ICMSTot.vDesc.valor   = '0.00'
    n.infNFe.total.ICMSTot.vII.valor     = '0.00'
    n.infNFe.total.ICMSTot.vIPI.valor    = '0.00'
    n.infNFe.total.ICMSTot.vPIS.valor    = '0.00'
    n.infNFe.total.ICMSTot.vCOFINS.valor = '0.00'
    n.infNFe.total.ICMSTot.vOutro.valor  = '0.00'
    n.infNFe.total.ICMSTot.vNF.valor     = '1000.00'
    n.gera_nova_chave()

    #
    # O retorno de cada webservice é um objeto
    # com as seguintes propriedades
    #  .webservice - o webservice que foi consultado
    #  .envio - o objeto da classe XMLNFE enviado
    #  .envio.original - o texto do xml (envelope SOAP) enviado ao webservice
    #  .resposta - o objeto da classe XMLNFE retornado
    #  .resposta.version - version da HTTPResponse
    #  .resposta.status - status da HTTPResponse
    #  .resposta.reason - reason da HTTPResponse
    #  .resposta.msg - msg da HTTPResponse
    #  .resposta.original - o texto do xml (SOAP) recebido do webservice
    #
    for processo in p.processar_notas([n]):
        print(processo)
        print()
        print(processo.envio.xml)
        print()
        print(processo.envio.original)
        print()
        print(processo.resposta.xml)
        print()
        print(processo.resposta.original)
        print()
        print(processo.resposta.reason)

        #
        # A consulta dos recibos também retorna dois dicionários, cujas chaves
        # são as chaves das NF-es enviadas;
        #    . dic_protNFe - dicionário com os protocolos de cada NF-e
        #    . dic_procNFe - dicionário com os processos (NF-e + protocolo) de cada NF-e
        #    cada procNFe tem ainda uma propriedade:
        #        .danfe_pdf - conteúdo binário do DANFE em PDF
        #
        if processo.webservice == WS_NFE_CONSULTA_RECIBO:
            print()
            print(processo.resposta.dic_protNFe)
            print()
            print(processo.resposta.dic_procNFe)

