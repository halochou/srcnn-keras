gt = imread('butterfly_GT.bmp');
gt = rgb2ycbcr(gt);
gt = gt(:,:,1);
gt = gt(7:231,7:231,1);
%gt = gt(7:255,7:255,1);

psnrs = [];
for i = 3200:50:14000
    fn = sprintf('outputs/%05d.png',i);
    ti = imread(fn);
    ti = ti(7:231,7:231,:);
    if size(ti,3) > 1
        ti = rgb2ycbcr(ti);
        ti = ti(:,:,1);
    end
    psnrs = [psnrs psnr(ti, gt)];
end