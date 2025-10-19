import React, {useEffect, useState} from 'react'


function AnalyticsPage() {
  const [products, setProducts] = useState(null);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('chair');

  useEffect(() => {
    setProducts(null);
    setError(null);
    fetch(`https://genaihackathon.aup.events:7500/recommend?query=${encodeURIComponent(searchTerm)}`)
      .then(r => {
        if (!r.ok) throw new Error('recommend fetch failed');
        return r.json();
      })
      .then(data => setProducts(data.recommendations || []))
      .catch(err => {
        console.error(err);
        setError(err.message);
      });
  }, [searchTerm]);

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  if (error) return <div className="alert alert-danger">Error loading products: {error}</div>;
  if (!products) return <div>Loading products...</div>;

  return (
    <div>
      <h3>Products ({products.length})</h3>
      <div className="mb-3">
        <input
          type="text"
          value={searchTerm}
          onChange={handleSearchChange}
          placeholder="Search for products (e.g. mat, chair)"
          className="form-control"
          style={{maxWidth: 300}}
        />
      </div>
      <div className="row">
        {products.map(p => {
          const title = p.title || p.name || 'Untitled';
          const brand = p.brand || 'Unknown';
          let displayedPrice = null;
          if (p.price_display) {
            displayedPrice = p.price_display;
          } else if (typeof p.price === 'number') {
            displayedPrice = `$${p.price.toFixed(2)}`;
          } else if (typeof p.price === 'string' && p.price.trim()) {
            const m = p.price.match(/-?[0-9,]*\.?[0-9]+/);
            if (m) {
              const n = Number(m[0].replace(/,/g, ''));
              displayedPrice = isNaN(n) ? p.price : `$${n.toFixed(2)}`;
            } else {
              displayedPrice = p.price;
            }
          } else {
            displayedPrice = '$0.00';
          }
          let imageRaw = p.image_url || p.image || p.imageUrl || p.images || null;
          let image = null;
          if (Array.isArray(imageRaw) && imageRaw.length) {
            image = imageRaw[0];
          } else if (typeof imageRaw === 'string' && imageRaw.trim()) {
            const s = imageRaw.trim();
            if (s.startsWith('[')) {
              try {
                const normalized = s.replace(/'/g, '"');
                const arr = JSON.parse(normalized);
                if (Array.isArray(arr) && arr.length) image = arr[0];
              } catch (err) {
                const m = s.match(/https?:\/\/[^\"]+/);
                if (m) image = m[0];
              }
            } else {
              const m = s.match(/https?:\/\/[^",\s\]]+/);
              if (m) image = m[0];
              else image = s;
            }
          }
          if (typeof image === 'string') image = image.trim();
          const imageUrl = image || '/placeholder.png';
          const aiDesc = p.ai_description || p.aiDescription || p.creative_description || '';

          return (
            <div key={p.uniq_id || p.id || title} className="col-md-4 mb-3">
              <div className="card h-100">
                {image ? (
                  <img src={image} className="card-img-top" alt={`Image of ${title}`} style={{ objectFit: 'cover', height: 180 }} />
                ) : (
                  <div className="bg-light d-flex align-items-center justify-content-center" style={{ height: 180 }}>No image</div>
                )}
                <div className="card-body d-flex flex-column">
                  <h5 className="card-title">{title}</h5>
                  <h6 className="text-muted mb-2">{brand}</h6>
                  <p className="mt-1 mb-2"><strong>{displayedPrice}</strong></p>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default AnalyticsPage;
