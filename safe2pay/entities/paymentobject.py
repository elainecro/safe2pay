# -*- coding: utf-8 -*-
from .lib import *

class PaymentObject(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}		

		# FIELDS
		# cls.Id = String(max=26)
		# cls.Identifier = String(max=26)
		# cls.IdTransaction = String(max=26)
		cls.Holder = String(max=25)
		cls.CardNumber = String(max=19)
		cls.ExpirationDate = String(max=7)
		cls.SecurityCode = String(max=4)
		cls.Token = String(max=42)
		cls.InstallmentQuantity = Int()
		cls.IsPreAuthorization = Boolean()
		cls.IsApplyInterest = Boolean()
		cls.Expiration = Int(max=10)
		# cls.InterestRate = Decimal(max=18,scale=2)
		cls.DueDate = DateTime(format="%d/%m/%Y")
		cls.Instruction = String(max=200)
		cls.Message = ObjList(context=cls, key='Message', name='str')
		cls.PenaltyRate = DecimalS2P(max=18)
		cls.InterestRate = DecimalS2P(max=18)
		cls.CancelAfterDue = Boolean()
		cls.DaysBeforeCancel = Int()
		cls.IsEnablePartialPayment = Boolean()
		cls.DiscountAmount = DecimalS2P(max=18)
		cls.DiscountType =  Int()
		cls.DiscountDue = DateTime(format="%d/%m/%Y")
		# cls.Description = String(max=200)
		# cls.Tid = String(max=200)
		# cls.AuthorizationCode = String(max=200)
		# cls.Status = Int()
		# cls.BankSlipNumber =  String(max=200)
		# cls.DigitableLine =  String(max=200)
		# cls.Barcode =  String(max=200)
		# cls.BankSlipUrl =  String(max=200)
		# cls.OperationDate =  DateTime(format="%d/%m/%Y")
		# cls.BankName =  String(max=200)
		# cls.CodeBank =  String(max=200)
		# cls.Wallet =  String(max=200)
		# cls.WalletDescription =  String(max=200)
		# cls.Agency =  String(max=200)
		# cls.Account =  String(max=200)
		# cls.CodeAssignor =  String(max=200)
		# cls.KeyPix =  String(max=200)
		# cls.AgencyDV =  String(max=200)
		# cls.AccountDV =  String(max=200)
		# cls.DocType =  String(max=200)
		# cls.Accept =  String(max=200)
		# cls.Currency =  String(max=200)
		# cls.GuarantorName =  String(max=200)
		# cls.GuarantorIdentity =  String(max=200)
		# cls.HasError = Boolean()
		# cls.Reference =  String(max=200)
		# cls.Key =  String(max=200)
		# cls.QrCode=  String(max=200)
		cls.DiscountPayment = DecimalS2P(max=18)
		cls.Command = Int()

		super().__init__(**kw)
