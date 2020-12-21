    def visitId(self,ctx,o):
        sym = [x for x in o.sym if x.name == ctx.name][0]
        if(o.isLeft):
            if type(sym.value) is not Index:
                return self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name, sym.mtype, o.frame), sym.mtype
            else:
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype           
        else:
            if type(sym.value) is not Index:
                return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, sym.mtype, o.frame), sym.mtype
            else:
                return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype