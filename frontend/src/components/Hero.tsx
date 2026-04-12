const Hero = () => {
  return (
    <>
      {/* Banner principal */}
      <section className="bg-slate-900 text-white py-16 px-8 flex flex-col md:flex-row items-center justify-between gap-8 relative overflow-hidden">
        {/* Círculo decorativo de fondo */}
        <div className="absolute w-96 h-96 rounded-full bg-sky-400/5 -top-24 -right-16 pointer-events-none" />

        {/* Texto */}
        <div className="z-10 max-w-xl">
          <span className="inline-block bg-sky-400/10 text-sky-400 text-xs font-semibold px-3 py-1 rounded-full border border-sky-400/30 mb-4">
            ⚡ Envío gratis en pedidos +$50
          </span>
          <h1 className="text-4xl md:text-5xl font-bold leading-tight mb-4">
            La mejor tecnología<br />
            en <span className="text-sky-400">Ecuador</span>
          </h1>
          <p className="text-slate-400 text-lg mb-8">
            Equipa tu setup con los mejores periféricos del mercado.
          </p>
          <div className="flex gap-4 flex-wrap">
            <button className="bg-sky-400 text-slate-900 px-7 py-3 rounded-lg font-semibold hover:bg-sky-300 transition-colors duration-200">
              Ver Catálogo
            </button>
            <button className="border border-slate-600 text-white px-7 py-3 rounded-lg font-semibold hover:border-slate-400 transition-colors duration-200">
              Ver Ofertas
            </button>
          </div>
        </div>

        {/* Estadísticas */}
        <div className="flex gap-10 z-10">
          {[
            { num: '10+', label: 'Productos' },
            { num: '100%', label: 'Garantía' },
            { num: '24h', label: 'Soporte' },
          ].map((s) => (
            <div key={s.label} className="text-center">
              <div className="text-3xl font-bold text-sky-400">{s.num}</div>
              <div className="text-xs text-slate-500 mt-1">{s.label}</div>
            </div>
          ))}
        </div>
      </section>

      {/* Franja de confianza */}
      <div className="bg-slate-800 py-3 px-8 flex gap-8 overflow-x-auto">
        {['Pago seguro', 'Devolución garantizada', 'Productos originales', 'Soporte local Ecuador', 'Envío a todo el país'].map((item) => (
          <div key={item} className="flex items-center gap-2 text-slate-400 text-sm whitespace-nowrap">
            <span className="w-1.5 h-1.5 rounded-full bg-sky-400 flex-shrink-0" />
            {item}
          </div>
        ))}
      </div>
    </>
  );
};

export default Hero;
